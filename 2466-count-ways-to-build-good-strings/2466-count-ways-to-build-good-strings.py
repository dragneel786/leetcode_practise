class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
#         @lru_cache(None)
#         def const_string(size):
#             nonlocal low, high, zero, one
#             if(size > high):
#                 return 0
            
#             return (1 + const_string(size + zero) +\
#                     const_string(size + one)) % MOD
        
#         MOD = 10 ** 9 + 7
#         return (const_string(zero) +\
#                 const_string(one)) % MOD

        MOD = 10 ** 9 + 7
        dp = [0] * (high + max(one, zero) + 1)
        for i in range(high, -1, -1):
            dp[i] = (dp[i + zero] + dp[i + one] + (i >= low)) % MOD
        
        return dp[0]
        
        