class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [([inf] * cols) for _ in range(rows)]
        
        for i in range(cols):
            dp[0][i] = matrix[0][i]
        
        for r in range(1, rows):
            for c in range(cols):
                for dr, dc in [(-1, 1), (-1, 0), (-1, -1)]:
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < rows and 0 <= nc < cols):
                        dp[r][c] = min(dp[r][c], matrix[r][c] + dp[nr][nc])
        
        return min(dp[-1])