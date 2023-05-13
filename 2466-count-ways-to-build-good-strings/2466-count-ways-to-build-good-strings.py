class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        @lru_cache(None)
        def const_string(size = 0):
            nonlocal low, high, zero, one
            if(size > high):
                return 0
            
            return ((size >= low) + const_string(size + zero)\
        + const_string(size + one)) % MOD
        
        MOD = 10 ** 9 + 7
        return const_string() % MOD