class Solution:
    def soupServings(self, n: int) -> float:
        
        @lru_cache(None)
        def empty_prob(a, b):
            if(a <= 0 and b <= 0):
                return 0.5
            
            if(a <= 0):
                return 1
            
            if(b <= 0):
                return 0
            
            return 0.25 * (empty_prob(a - 100, b)\
                           + empty_prob(a - 75, b - 25)\
                           + empty_prob(a - 50, b - 50)\
                           + empty_prob(a - 25, b - 75))
        
        return 1 if(n >= 4800) else empty_prob(n, n)