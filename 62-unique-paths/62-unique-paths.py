class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [([0] * n) for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if(r == m - 1 and c == n - 1): continue
                val = 0
                if(r + 1 < m): val += dp[r + 1][c]
                if(c + 1 < n): val += dp[r][c + 1]
                dp[r][c] = val
        return dp[0][0]