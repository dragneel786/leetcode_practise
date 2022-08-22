class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n < 4): return n == 1
        
        bits_needed = int(log(n) / log(2))
        return ((1 << bits_needed) ^ n) == 0 and (bits_needed + 1) & 1 == 1