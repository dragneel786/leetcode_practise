class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        coins.sort()
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if(c <= i):
                    dp[i] += dp[i - c]
        return dp[amount]