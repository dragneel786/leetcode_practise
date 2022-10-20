class Solution:
    def reverse(self, x: int) -> int:
        signed = True if(x < 0) else False
        limit = 2 ** 31
        val = 0
        x *= -1 if(signed) else 1
        while(x):
            mod = x % 10
            x //= 10
            val *= 10
            if(signed and (val + mod) > limit):
                return 0
            
            if(not signed and (val + mod) > limit - 1):
                return 0
            
            val += mod
        
        return val * (-1 if(signed) else 1)
        