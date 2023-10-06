class Solution:
    def integerBreak(self, n: int) -> int:
        if(n < 4):
            return n - 1
        
        pro = 1
        while(n > 4):
            pro *= 3
            n -= 3
        return pro * n
        
        
        