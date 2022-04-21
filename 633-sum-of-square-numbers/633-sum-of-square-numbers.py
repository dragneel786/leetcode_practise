class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, h = 0, int(c ** 0.5)
        while(l <= h):
            val = l * l + h * h
            if(val == c):
                return True
            if(val > c):
                h -= 1
            else:
                l += 1

        return False