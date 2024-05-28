func equalSubstring(s string, t string, maxCost int) int {
    var dp = []int{}
    for i := 0; i < len(t); i++ {
        var diff = int(math.Abs(float64(int(s[i]) - int(t[i]))))
        dp = append(dp, diff)
    }
    
    var start, end, res = 0, 0, 0
    var currWindow = 0
    for end < len(dp) {
        currWindow += dp[end]
        for currWindow > maxCost {
            currWindow -= dp[start]
            start++
        }
        res = max(res, end - start + 1)
        end++
    }
    
    return res
}