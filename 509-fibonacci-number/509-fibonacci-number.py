class Solution:
    def fib(self, n: int) -> int:
        if(n == 0):
            return 0
        
        f1 = 0
        f2 = 1
        for i in range(n - 1):
            f1, f2 = f2, f1 + f2
            
        return f2