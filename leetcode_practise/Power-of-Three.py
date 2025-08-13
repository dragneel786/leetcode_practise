class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        val = 1
        while(val < n):
            val *= 3
        
        return val == n
