class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y, visited = set()):
            visited.add((x, y))
            res = 0
            for dx, dy in [(0, 1), (1, 0),\
                           (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if(0 <= nx < m and 0 <= ny < n and grid[nx][ny]):
                    if((nx, ny) in visited):
                        continue
                    res += dfs(nx, ny)
                else:
                    res += 1
                      
            return res
        
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if(grid[r][c]):
                    return dfs(r, c)
        