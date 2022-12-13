class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [inf] * cols
        
        for i in range(cols):
            dp[i] = matrix[0][i]
        
        for r in range(1, rows):
            ndp = [inf] * cols
            for c in range(cols):
                for dc in [1, 0, -1]:
                    nc = c + dc
                    if(0 <= nc < cols):
                        ndp[c] = min(ndp[c], matrix[r][c] + dp[nc])
            
            dp = ndp
        
        return min(dp)