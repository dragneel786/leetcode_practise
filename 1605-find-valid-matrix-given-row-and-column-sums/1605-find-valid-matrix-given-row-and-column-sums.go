func restoreMatrix(rowSum []int, colSum []int) [][]int {
    var ret = [][]int{}
    var rows, cols = len(rowSum), len(colSum)
    for i := range rows {
        ret = append(ret, make([]int, cols))
        ret[i][0] = rowSum[i]
    }
    
    for c := range cols - 1{
        for r := range rows {
            if ret[r][c] <= colSum[c] {
                colSum[c] -= ret[r][c]
            } else {
                ret[r][c + 1] = (ret[r][c] - colSum[c])
                ret[r][c] = colSum[c]
                colSum[c] = 0
            }
        }
    }
    
    return ret
}