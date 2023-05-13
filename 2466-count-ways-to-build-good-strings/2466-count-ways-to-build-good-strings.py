class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        @lru_cache(None)
        def const_string(size):
            nonlocal low, high, zero, one
            if(size > high):
                return 0
            
            return ((size >= low) + const_string(size + zero) +\
                    const_string(size + one)) % MOD
        
        MOD = 10 ** 9 + 7
        return (const_string(zero) +\
                const_string(one)) % MOD

#         MOD = 10 ** 9 + 7
#         dp = [0] * (high + max(zero, one) + 1)
#         for i in range(high, low - 1, -1):
#             dp[i] = (dp[i + zero] + dp[i + one] + 1) % MOD
        
#         print(dp)
#         return dp[low]
        