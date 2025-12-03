class Solution:
    def sumAndMultiply(self, n: int) -> int:
        mul = tot = 0
        pows = 1
        while(n):
            rem = n % 10
            if rem != 0:
                mul = (pows * rem) + mul
                tot += rem
                pows *= 10
            n //= 10
        
        return tot * mul