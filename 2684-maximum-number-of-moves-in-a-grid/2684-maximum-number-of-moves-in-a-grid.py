class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [([0] * cols) for _ in range(rows)]
        for r in range(rows):
            dp[r][0] = 1
        
        max_val = 0
        for c in range(1, cols):
            for r in range(rows):
                path = 0
                for dr, dc in [(-1,-1), (0,-1), (1,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and \
                    grid[nr][nc] < grid[r][c] and dp[nr][nc] > 0:
                        path = max(path, dp[nr][nc] + 1)
                
                dp[r][c] = path        
                max_val = max(max_val, path - 1)
        
        return max_val
                    
                    
                    
                
        
        
        
        
        