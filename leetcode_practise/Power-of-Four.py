class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4:
            return n == 1
        
        return (n & (n - 1) == 0) and len(bin(n)) % 2 == 1