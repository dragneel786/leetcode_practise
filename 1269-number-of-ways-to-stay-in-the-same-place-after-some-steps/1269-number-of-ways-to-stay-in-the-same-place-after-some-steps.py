class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def ways(idx, remain):
            nonlocal MOD
            if(idx < 0 or idx >= arrLen):
                return 0
            
            if(remain == 0):
                return idx == 0
            
            left = ways(idx - 1, remain - 1)
            right = ways(idx + 1, remain - 1)
            stay = ways(idx, remain - 1)
            return (left + stay + right) % MOD
        
        MOD = (10 ** 9) + 7
        return ways(0, steps) % MOD
        