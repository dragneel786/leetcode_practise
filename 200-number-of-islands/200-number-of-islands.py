class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            grid[x][y] = '0'
            for dx, dy in [(1, 0), (0, 1),\
                           (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if(0 <= nx < rows and 0 <= ny
                   < cols and grid[nx][ny] == '1'):
                    dfs(x + dx, y + dy)
        
        counts = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == '1'):
                    counts += 1
                    dfs(r, c)
                    
        return counts