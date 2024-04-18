func islandPerimeter(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
	
	set := make(map[[2]int]bool)
    
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++{
            if grid[r][c] == 1 {
                return findPerimeter(grid, r, c, set)
            }
        }
    }
    return 0
}

func findPerimeter(grid [][]int, sr, sc int, set map[[2]int]bool) int{
    rows := len(grid)
    cols := len(grid[0])
	coor := [2]int {sr, sc}

	if set[coor] {
		return 0
	}

    if (sr < 0 || sr >= rows || 
        sc < 0 || sc >= cols || 
        grid[sr][sc] == 0){   
        return 1
    }

	set[coor] = true
    dire := [5]int {0, 1, 0, -1, 0}
    var ret int;
    for i := range dire[:len(dire) - 1]{
		
        ret += findPerimeter(grid, sr + dire[i], sc + dire[i + 1], set)
    }
    return ret
}