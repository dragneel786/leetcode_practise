class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y) -> bool:
            if(x < 0 or y < 0 or x >= m or y >= n):
                return False
            
            if(grid[x][y]):
                return True
            
            grid[x][y] = -1
            return sum(dfs(x + dx, y + dy) for dx, dy in dic) == 4
        
        dic = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        counts = 0
        for i in range(m):
            for j in range(n):
                if(not grid[i][j]):
                    counts += dfs(i, j)
        return counts