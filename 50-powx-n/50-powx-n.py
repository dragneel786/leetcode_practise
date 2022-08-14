class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0): return 1
        
        is_div = False
        if(n < 0):
            n = -1 * n
            is_div = True
        val = self.myPow(x, n // 2)
        val = val * val
        if(n % 2):
            val *= x
            
        return  1 / val if(is_div) else val