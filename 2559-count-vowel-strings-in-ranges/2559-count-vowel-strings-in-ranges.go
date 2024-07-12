func vowelStrings(words []string, queries [][]int) []int {
    var size = len(words)
    var vowelCount = make([]int, size)
    var vowels = make(map[byte]bool)
    for _, c := range "aeiou" { vowels[byte(c)] = true }
    
    var prev = 0
    for i := range size {
        if vowels[words[i][0]] && vowels[words[i][len(words[i]) - 1]] {
            vowelCount[i] += 1
        }
        vowelCount[i] += prev
        prev = vowelCount[i]
    }
    
    var ret = []int{}
    for _, query := range queries {
        var ans = vowelCount[query[1]]
        if query[0] > 0 {
            ans -= vowelCount[query[0] - 1]
        }
        ret = append(ret, ans)
    }
    return ret
}