class Solution:
    def numTilings(self, n: int) -> int:
        
        dp = [0] * (n + 4)
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
        
        return dp[n] % (10 ** 9 + 7)
        