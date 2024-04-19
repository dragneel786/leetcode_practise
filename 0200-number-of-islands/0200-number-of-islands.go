func numIslands(grid [][]byte) int {
    fmt.Println(grid)
    islands := 0
    for r := range grid {
        for c := range grid[0] {
            if grid[r][c] == '1' {
                traverse(grid, r, c)
                islands += 1
            }
        }
    }
    return islands
}


func traverse(grid [][]byte, sr, sc int) {
    grid[sr][sc] = '0'
    rows, cols := len(grid), len(grid[0])
    dir := []int{0, 1, 0, -1, 0}
    for i := range dir[:len(dir) - 1]{
        nr, nc := sr + dir[i], sc + dir[i + 1]
        if (nr >= 0 && nr < rows && 
            nc >= 0 && nc < cols && 
            grid[nr][nc] == '1') {
            traverse(grid, nr, nc)
        }
    }
}

