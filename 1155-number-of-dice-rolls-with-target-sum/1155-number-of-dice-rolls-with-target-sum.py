class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def ways(n, val = 0):
            nonlocal k, target, MOD
            if(n < 0 or val >= target):
                return val == target and n == 0
            
            res = 0
            for face in range(1, k + 1):
                res += ways(n - 1, val + face)
            
            return (res % MOD)
        
        MOD = 10 ** 9 + 7
        return ways(n) % MOD
        
        
        
            
            
            
            