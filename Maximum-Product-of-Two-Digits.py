class Solution:
    def maxProduct(self, n: int) -> int:
        values = []
        while(n):
            values.append(n % 10)
            n //= 10
        
        values.sort()
        return values[-1] * values[-2]