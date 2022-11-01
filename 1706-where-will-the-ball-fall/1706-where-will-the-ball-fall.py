class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        memo = [[c for c in range(cols)]\
                for _ in range(rows + 1)]
        
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                nc = c + grid[r][c]
                if(nc < 0 or nc == cols or \
                   grid[r][c] != grid[r][nc]):
                    memo[r][c] = -1
                    continue
                
                memo[r][c] = memo[r + 1][nc]
        
        return memo[0]
                
                
                
        
        
            