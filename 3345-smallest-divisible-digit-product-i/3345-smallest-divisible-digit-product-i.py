class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for val in range(max(n, t), 101):
            temp = val
            prod = 1
            while(val):
                mod = val % 10
                prod *= mod
                val //= 10
            
            if (prod % t) == 0:
                return temp
        