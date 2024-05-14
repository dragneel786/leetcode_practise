func getMaximumGold(grid [][]int) int {
    var rows, cols = len(grid), len(grid[0])
    var ret = 0
    for r := range rows {
        for c := range cols {
            if grid[r][c] != 0 {
                ret = max(ret, grid[r][c] + maxPossibleGold(&grid, r, c))
            }
        }
    }
    return ret
}


func maxPossibleGold(grid *[][]int, r, c int) int {
	var value = (*grid)[r][c]
	(*grid)[r][c] = 0
	
    var dr = []int{1, 0, -1, 0, 1}
    var rows, cols = len(*grid), len((*grid)[0])
    
    var res = 0
    for i := range 4 {
        var nr, nc = r + dr[i], c + dr[i + 1]
        
        if (nr < rows && nr >= 0 && nc < cols && nc >= 0 && (*grid)[nr][nc] > 0) {
            res = max(res, (*grid)[nr][nc] + maxPossibleGold(grid, nr, nc))
        }
        
    }
    (*grid)[r][c] = value
    return res
}