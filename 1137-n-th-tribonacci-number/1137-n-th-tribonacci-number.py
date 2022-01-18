class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for _ in range(n):
            dp[0], dp[1], dp[2] = dp[1], dp[2], \
            dp[0] + dp[1] + dp[2]
            
        return dp[0]