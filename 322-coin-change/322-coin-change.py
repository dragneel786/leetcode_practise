class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for a in range(1, amount + 1):
            for c in coins:
                if((a - c) < 0):
                    break
                dp[a] = min(dp[a - c] + 1, dp[a])
        
        return dp[amount] if(dp[amount] != math.inf) else -1