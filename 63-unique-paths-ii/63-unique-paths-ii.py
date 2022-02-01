class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if(obstacleGrid[0][0] or obstacleGrid[rows - 1][cols - 1]):
            return 0
        
        dp = [([0] * cols) for _ in range(rows)]
        dp[rows - 1][cols - 1] = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if((r != rows - 1 or c != cols - 1) and not obstacleGrid[r][c]):
                    if(r + 1 < rows):
                        dp[r][c] += dp[r + 1][c]
                    if(c + 1 < cols):
                        dp[r][c] += dp[r][c + 1]
        
        return dp[0][0]
                    