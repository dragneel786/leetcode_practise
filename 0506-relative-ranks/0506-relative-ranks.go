func findRelativeRanks(score []int) []string {
    posMap := make(map[int]int)
    for i, s := range score {
        posMap[s] = i
    }
    
    slices.SortFunc(score, func(a, b int) int { 
        return b - a
    })
    ans := make([]string, len(score))
    for i, s := range score {
        idx := posMap[s]
        switch i {
            case 0:
                ans[idx] = "Gold Medal"
            case 1:
                ans[idx] = "Silver Medal"
            case 2:
                ans[idx] = "Bronze Medal"
            default:
                ans[idx] = strconv.Itoa(i + 1)
        }
    }
    return ans
}