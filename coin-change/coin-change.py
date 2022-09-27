class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        dp = [inf] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if(a < coin): break
                dp[a] = min(dp[a - coin] + 1, dp[a])
        
        return dp[amount] if(dp[amount] != inf) else -1