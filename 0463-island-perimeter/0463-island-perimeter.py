class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def sub_direction(x, y):
            nonlocal ans
            for dx, dy in [(0, 1), (0, -1),\
                           (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if(0 <= nx < m and 0 <= ny < n and grid[nx][ny]):
                    ans -= 1
        
        m, n = len(grid), len(grid[0])
        ans = 0
        for r in range(m):
            for c in range(n):
                if(grid[r][c]):
                    ans += 4
                    sub_direction(r, c)
        
        return ans
        