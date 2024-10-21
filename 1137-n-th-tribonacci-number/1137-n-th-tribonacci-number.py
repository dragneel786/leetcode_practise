class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return n if n < 2 else 1
        
        t0, t1, t2 = 0, 1, 1
        for i in range(2, n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        
        return t2