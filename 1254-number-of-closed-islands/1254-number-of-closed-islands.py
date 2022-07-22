class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y) -> bool:
            if(x < 0 or y < 0 or x >= m or y >= n):
                return False
            
            if(grid[x][y]):
                return True
            
            grid[x][y] = -1
            res = True
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if(not dfs(nx, ny)):
                    res = False
            return res
            
        
        m = len(grid)
        n = len(grid[0])
        counts = 0
        for i in range(m):
            for j in range(n):
                if(not grid[i][j]):
                    counts += dfs(i, j)
        return counts