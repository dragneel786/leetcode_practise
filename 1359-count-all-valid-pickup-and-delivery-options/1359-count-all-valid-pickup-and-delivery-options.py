class Solution:
    def countOrders(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = (i * dp[i - 1] * ((2 * i) - 1)) % (10 ** 9 + 7)
        
        return dp[n]
        