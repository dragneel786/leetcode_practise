class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        ans = 0
        for x in range(m):
            for y in range(n):
                for dx, dy in [(0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if(0 <= nx < m and 0 <= ny < n):
                        ans += grid[x][y] != grid[nx][ny]
                    else:
                        ans += grid[x][y]
                        
        for x in range(n):
            ans += grid[m - 1][x]
            
        for y in range(m):
            ans += grid[y][n - 1]
                        
        return ans
        