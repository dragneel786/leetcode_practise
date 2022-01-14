class Solution:
    def coinChange(self, coins: List[int], amount: int, memo = {}) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            minVal = float('inf')
            for coin in coins:
                idx = i - coin
                if(idx >= 0 and dp[idx] >= 0):
                    minVal = min(minVal, 1 + dp[idx])

            if(minVal != float("inf")):
                dp[i] = minVal

        return dp[amount]