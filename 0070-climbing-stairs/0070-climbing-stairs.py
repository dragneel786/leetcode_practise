class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        def climb_it(n):
            if(n <= 0):
                return n == 0
            
            if(n in cmap):
                return cmap[n]
            
            cmap[n] = climb_it(n - 1) + climb_it(n - 2)
            return cmap[n]
        
        cmap = dict()
        return climb_it(n)