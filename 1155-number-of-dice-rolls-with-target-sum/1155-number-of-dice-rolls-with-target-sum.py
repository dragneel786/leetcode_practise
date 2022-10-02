class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        def roll_it(n, s = 0):
            nonlocal target, k
            if(s == target and n == 0):
                return 1
            
            if(s >= target or n <= 0):
                return 0
            
            key = (n, s)
            if(key in memo): return memo[key]
            
            count = 0
            for i in range(1, k + 1):
                count += roll_it(n - 1, s + i)
                count %= MOD
            
            memo[key] = count
            return memo[key]
        
        memo = {}
        MOD = (10 ** 9) + 7
        return roll_it(n)
        
                