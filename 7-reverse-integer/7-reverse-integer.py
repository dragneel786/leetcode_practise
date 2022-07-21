class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if(x < 0) else 1
        bound = 2**31 - 1
        rev = 0
        x = abs(x)
        while(x):
            rem = x % 10
            if(sign == 1 and ((rev > bound // 10) or (rev == bound // 10 and rem > 7))): return 0
            if((sign == -1) and ((rev > (bound + 1) // 10)\
                     or ((rev == (bound + 1) // 10) and (rem > 8)))): return 0
            rev = (rev * 10) + rem
            x //= 10
               
        return rev * sign