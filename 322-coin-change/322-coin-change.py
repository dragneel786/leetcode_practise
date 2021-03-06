class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        coins.sort()
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if(i - c < 0):
                    break
                dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[-1] if(dp[-1] != math.inf) else -1