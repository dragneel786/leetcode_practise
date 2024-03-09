class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            nonlocal grid, m, n
            ret = grid[r][c]
            grid[r][c] = 0
            for dr, dc in [(0,1), (1,0),
                           (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if(0 <= nr < m and \
                   0 <= nc < n and \
                   grid[nr][nc]):
                    
                    ret += dfs(nr, nc)
            
            return ret
                    
        
        
        
        m, n = len(grid), len(grid[0])
        max_fish = 0
        for r in range(m):
            for c in range(n):
                if(grid[r][c]):
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish
                
            
        
                
        