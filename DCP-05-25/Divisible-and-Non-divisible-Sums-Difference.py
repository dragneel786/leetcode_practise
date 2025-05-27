class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = (n * (n + 1)) // 2
        mul = num2 = 0
        while(mul * m <= n):
            num1 -= (mul * m)
            num2 += (mul * m)
            mul += 1
        
        return num1 - num2