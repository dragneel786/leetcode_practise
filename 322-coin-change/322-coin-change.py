class Solution:
    def coinChange(self, coins: List[int], amount: int, memo = {}) -> int:
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for coin in coins:
                idx = i - coin
                if(idx < 0):
                    break
                
                if(dp[idx] != amount + 1):
                    dp[i] = min(dp[i], 1 + dp[idx])
            
                    
        return dp[amount] if (dp[amount] != amount + 1) else -1