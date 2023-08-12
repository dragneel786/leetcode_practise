class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [([0] * (n + 1)) for _ in range(m + 1)]
        dp[m - 1][n - 1] += obstacleGrid[m - 1][n - 1] != 1
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] += obstacleGrid[r][c] != 1\
                and dp[r][c + 1] + dp[r + 1][c]
                
        
        return dp[0][0]