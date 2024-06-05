func commonChars(words []string) []string {
    var maxOccList = make([]int, 26)
    for i, word := range words {
        var commons = make(map[rune]int)
        for _, c := range word {
            commons[c]++
        }
        
        for k := range 26 {
            if i == 0 {
                maxOccList[k] = commons[rune(k + 97)]
            } else {
                maxOccList[k] = min(commons[rune(k + 97)], maxOccList[k])
            }
        }
    }
    
    var res = []string{}
    for i, v := range maxOccList {
        for range v {
            res = append(res, string(i + 97))
        }
    }
    return res
}