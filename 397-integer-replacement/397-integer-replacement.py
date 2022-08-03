class Solution:
    def integerReplacement(self, n: int) -> int:
        
        @lru_cache(None)
        def getSteps(num):
            if(num == 2): return 1
            if(num == 1): return 0
            
            return 1 + (min(getSteps(num - 1), getSteps(num + 1))\
        if(num & 1) else getSteps(num // 2))
        
        return getSteps(n)
    