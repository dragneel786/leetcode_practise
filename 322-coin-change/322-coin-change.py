class Solution:
    def coinChange(self, coins: List[int], amount: int, memo = {}) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            minVal = float('inf')
            for coin in coins:
                idx = i - coin
                if(idx >= 0 and dp[idx] >= 0):
                    minVal = min(minVal, 1 + dp[idx])

            dp[i] = minVal if(minVal != float("inf")) else -1

        return dp[amount]