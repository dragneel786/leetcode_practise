class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        @lru_cache(None)
        def get_ways(size = 0):
            if size > high:
                return 0

            return (get_ways(size + zero) + get_ways(size + one) + (size >= low)) % MOD
        
        MOD = (10 ** 9) + 7
        return get_ways(0)