class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for d in range(1, 12):
            f = 10 ** (d - 1)
            if(n < 9 * f * d):
                return int(str(f + (n // d))[n % d])
            n -= (9 * f * d)