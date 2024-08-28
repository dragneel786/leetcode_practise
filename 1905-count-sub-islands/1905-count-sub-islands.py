class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        
        def dfs(sr, sc):
            d = [0,1,0,-1,0]
            ret = []
            for i in range(4):
                nr, nc = sr + d[i], sc + d[i + 1]
                if -1 < nr < rows and -1 < nc < cols and grid2[nr][nc]:
                    grid2[nr][nc] = 0
                    ret.append(dfs(nr, nc))
            
            return all(ret) and grid1[sr][sc] == 1
                    
                    
        rows, cols = len(grid1), len(grid1[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == grid2[r][c] == 1:
                    res += dfs(r, c)
        
        return res
            