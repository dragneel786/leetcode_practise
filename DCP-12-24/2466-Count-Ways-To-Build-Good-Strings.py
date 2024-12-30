class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = (10 ** 9) + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            way = 0
            if i - zero > -1:
                way = (way + dp[i - zero]) % MOD
            
            if i - one > -1:
                way = (way + dp[i - one]) % MOD
            
            dp[i] = way
        
        return sum(dp[low: high + 1]) % MOD