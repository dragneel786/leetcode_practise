class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            for dx, dy in [[1, 0], [-1, 0],\
                           [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if(0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1'):
                    grid[nx][ny] = '0'
                    dfs(nx, ny)
        
        m, n = len(grid), len(grid[0])
        islands_count = 0
        
        for r in range(m):
            for c in range(n):
                if(grid[r][c] == '1'):
                    dfs(r, c)
                    islands_count += 1
        
        return islands_count
                    