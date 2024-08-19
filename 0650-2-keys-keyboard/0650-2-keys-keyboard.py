class Solution:
    def minSteps(self, n: int) -> int:
        sums, d = 0, 2
        while d * d <= n:
            while n % d == 0:
                n //= d
                sums += d
            d += 1
        
        return sums + (n if n > 1 else 0)