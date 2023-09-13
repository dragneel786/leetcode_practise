class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(num, base):
            res = []
            while(num > 0):
                mod = num % base
                num //= base
                res.append(mod)
            
            return res == reversed(res)
        
        for b in (2, n - 1):
            if(not convert(n, b)):
                return False
                
        return True