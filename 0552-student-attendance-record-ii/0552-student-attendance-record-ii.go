func checkRecord(n int) int {
    var dpInit = func() [][]int {
        return [][]int{{0, 0, 0}, {0, 0, 0}}
    }
    
    var MOD = int(math.Pow(10, 9)) + 7
    var dpCurrState = dpInit()
    dpCurrState[0][0] = 1
    var dpNextState = dpInit()
    
    for range n {
        for absense := range 2 {
            for late := range 3 {
                dpNextState[absense][0] = (dpNextState[absense][0] +
                                           dpCurrState[absense][late]) % MOD
                
                if absense < 1 {
                    dpNextState[absense + 1][0] = (
                        dpNextState[absense + 1][0] +
                        dpCurrState[absense][late]) % MOD
                }
                
                if late < 2 {
                    dpNextState[absense][late + 1] = (
                        dpNextState[absense][late + 1] +
                        dpCurrState[absense][late]) % MOD
                }
            }
        }
        dpCurrState = dpInit()
        copy(dpCurrState, dpNextState)
        dpNextState = dpInit()
    }
    var counts = 0
    for r := range 2 {
        for c := range 3 { 
            counts += dpCurrState[r][c]
        } 
    }
    
    return counts % MOD
}