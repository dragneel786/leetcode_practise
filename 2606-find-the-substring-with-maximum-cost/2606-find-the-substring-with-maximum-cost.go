func maximumCostSubstring(s string, chars string, vals []int) int {
    var charMap = make(map[rune]int)
    for i, c := range chars {
        charMap[c] = vals[i]
    }
    
    var charIntSub = []int{}
    for _, c := range s {
        var val = int(c) - 96
        if _, ok := charMap[c]; ok {
            val = charMap[c]
        }
        charIntSub = append(charIntSub, val)
    }
    
    var maxSoFar, maxCurr = 0, 0
    for _, a := range charIntSub {
        maxCurr = max(maxCurr + a, a)
        maxSoFar = max(maxSoFar, maxCurr)
    }
    
    return maxSoFar
}