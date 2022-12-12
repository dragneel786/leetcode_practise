class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def climb_it(n):
            if(n <= 0):
                return n == 0
            
            return climb_it(n - 1) + climb_it(n - 2)
        
        return climb_it(n)