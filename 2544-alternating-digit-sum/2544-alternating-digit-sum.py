class Solution:
    def alternateDigitSum(self, n: int) -> int:
        tot = 0
        sign = 1 if(len(str(n)) % 2) else -1
        while(n):
            remain = sign * (n % 10)
            n //= 10
            tot += remain
            sign *= -1
        
        return tot