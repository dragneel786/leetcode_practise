class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow_it(x, ns):
            if(ns == 0):
                return 0
            
            if(ns == 1):
                return x
            
            val = pow_it(x, ns // 2)
            val = val * val
            if(ns % 2):
                val *= x
            return val
        
        if(n == 0):
            return 1
        
        ret = pow_it(x, abs(n))
        return ret if(n >= 0) else 1/ret