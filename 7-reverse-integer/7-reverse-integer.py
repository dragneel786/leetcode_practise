class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if(x < 0) else 1
        rev = 0
        x = abs(x)
        while(x):
            rem = x % 10
            rev = (rev * 10) + rem
            x //= 10
        
        bound = 2**31
        return sign * rev if(-bound <= rev < bound) else 0