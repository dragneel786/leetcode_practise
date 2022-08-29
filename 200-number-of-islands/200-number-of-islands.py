class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            if(x < 0 or x >= rows or y < 0\
               or y >= cols or grid[x][y] == '0'):
                return
            
            grid[x][y] = '0'
            for dx, dy in [(1, 0), (0, 1),\
                           (-1, 0), (0, -1)]:
                dfs(x + dx, y + dy)
        
        
        counts = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1'):
                    counts += 1
                    dfs(r, c)
                    
        return counts