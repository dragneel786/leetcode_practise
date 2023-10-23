class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while(floor(n) > 1):
            n /= 4
            # print(n)
        return n == 1
        