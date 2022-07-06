class Solution:
    def fib(self, n: int) -> int:
        
        @functools.lru_cache(None)
        def getFib(n):
            if(n < 2):
                return n
            return getFib(n - 1) + getFib(n - 2)
        
        return getFib(n)