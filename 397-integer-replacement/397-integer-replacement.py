class Solution:
    def integerReplacement(self, n: int) -> int:
        
        def getSteps(num, memo = {1: 0, 2: 1}):
            if(num in memo): return memo[num]
            
            val = min(getSteps(num - 1), getSteps(num + 1)) if(num & 1)\
            else getSteps(num // 2)
            
            memo[num] = val + 1
            return val + 1
        
        return getSteps(n)
    