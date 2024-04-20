func findFarmland(land [][]int) [][]int {
    var res [][]int
    for r, hectareRows := range land {
        for c, hect := range hectareRows {
            if hect == 1 {
                br, bc := landCoor(land, r, c)
                res = append(res, []int{r, c, br, bc})
            }
        }
    } 
    return res
}

func landCoor(land [][]int, sr, sc int) (int, int) {
    
    rows, cols := len(land), len(land[0])
    maxR, maxC := sr, sc
    dir := []int{0, 1, 0, -1, 0}
    land[sr][sc] = 0
    for i := range dir[:len(dir) - 1] {
        nr, nc := sr + dir[i], sc + dir[i + 1]
        if (nr >= 0 && nc >= 0 && nr < rows && nc < cols && land[nr][nc] == 1){
            
            mr, mc := landCoor(land, nr, nc)
            if(maxR < mr || maxC < mc){
                maxR, maxC = mr, mc
            }
        }
    }
    return maxR, maxC
}