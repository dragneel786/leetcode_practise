class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [([0] * n) for _ in range(m)]
        dp[m - 1][n - 1] += obstacleGrid[m - 1][n - 1] != 1
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if(obstacleGrid[r][c]):
                    continue
                
                a, b = 0, 0
                if(r + 1 < m):
                    a = dp[r + 1][c]
                    
                if(c + 1 < n):
                    b = dp[r][c + 1]
                
                dp[r][c] += a + b
                
        
        return dp[0][0]