func minimumPushes(word string) int {
    var charMap = make([]int, 26)
    for _, c := range word {
        charMap[byte(c) - 97]++
    }
    sort.Slice(charMap, func(i, j int) bool {
        return charMap[j] < charMap[i]
    })
    var res = 0
    for i, v := range charMap {
        if v == 0 { break }
        res += ((i / 8) + 1) * v
    }
    return res
}