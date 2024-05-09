func maximumHappinessSum(happiness []int, k int) int64 {
    slices.SortFunc(happiness, func(a, b int) int{
        return b - a
    })
    
    upset := 0
    var ans int = 0
    for _, h := range happiness {
        if upset >= h || k == 0{
            break
        }
        ans += (h - upset)
        upset++
        k--
    }
    
    return int64(ans)
}