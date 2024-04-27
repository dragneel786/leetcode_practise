func findRotateSteps(ring string, key string) int {
    keyLen, ringLen := len(key), len(ring)
    dp := make([][]int, keyLen + 1)
    for i := range keyLen + 1 {
        dp[i] = make([]int, ringLen)
    }
    
    for k := keyLen - 1; k > -1; k-- {
        for r := range ringLen {
            
            minRot := math.MaxInt
            for i, c := range ring {
                if(c == rune(key[k])) {
                    diff := int(math.Abs(float64(r - i)))
                    minRot = min(minRot, min(diff, 
                        ringLen - diff) + dp[k + 1][i] + 1)
                }
            }
            
            dp[k][r] = minRot
        }
    }
    return dp[0][0]
}