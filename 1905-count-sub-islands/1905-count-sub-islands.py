class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(sr, sc):
            ret = True
            for dr, dc in [(1,0), (0,1), \
                           (-1,0), (0,-1)]:
                nr, nc = sr + dr, sc + dc
                if(0 <= nr < rows and 0 <= nc < cols):
                    ret = ret and (not (grid1[nr][nc] == 0 and grid2[nr][nc] == 1))
                    if(grid2[nr][nc] == 1):
                        grid2[nr][nc] = 0
                        ret = dfs(nr, nc) and ret

            return ret
        
        
        rows, cols = len(grid1), len(grid1[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if(grid2[row][col] == \
                   grid1[row][col] == 1):
                    grid2[row][col] = 0
                    ans += dfs(row, col)
        
        return ans
        