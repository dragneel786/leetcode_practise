func largestLocal(grid [][]int) [][]int {
    n := len(grid)
    res := [][]int{}
    for range n - 2 {
        res = append(res, make([]int, n - 2))
    }
    
    for r := 1; r < n - 1; r++ {
        for c := 1; c < n - 1; c++ {
            res[r - 1][c - 1] = grid[r][c]
            for _, dir := range [][]int{{1,0}, {0,1}, {-1,0}, {0,-1},
                                     {-1,-1}, {1,-1}, {-1,1}, {1,1}} {
                
                res[r - 1][c - 1] = max(res[r - 1][c - 1], 
                                        grid[r + dir[0]][c + dir[1]])
            }
        }
    }
    return res
}