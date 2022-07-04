class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def paint(i, j):
            if(min(i, j) < 0 or max(i, j) >= n or grid[i][j] != 1):
                return
            grid[i][j] = 2
            for dx, dy in dire:
                paint(i + dx, j + dy)
        
        def expand(i, j):
            if(min(i, j) < 0 or max(i, j) >= n or grid[i][j] == p):
                return False
            grid[i][j] = 1 if(grid[i][j] == 1) else p + 1
            return grid[i][j] == 1
        
        
        dire = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        for r in range(n):
            found = False
            for c in range(n):
                if(grid[r][c]):
                    paint(r, c)
                    found = True
                    break
            if(found):
                break
        
        for g in grid:
            print(g)
            
        for p in range(2, 1000):
            for r in range(n):
                for c in range(n):
                    for dx, dy in dire:
                        if(grid[r][c] == p and expand(r + dx, c + dy)):
                            return p - 2