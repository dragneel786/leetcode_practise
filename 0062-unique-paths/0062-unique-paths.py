class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(n - 2, -1, -1):
                dp[j] = dp[j + 1] + dp[j]
        return dp[0]