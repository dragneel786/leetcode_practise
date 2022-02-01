class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [([0] * n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(i == 0 and j == 0):
                    dp[i][j] = 1
                else:
                    for di, dj in [[-1, 0], [0, -1]]:
                        if(i + di > -1 and j + dj > -1):
                            dp[i][j] += dp[i + di][j + dj]
        return dp[m - 1][n - 1]