class Solution:
    def smallestNumber(self, n: int) -> int:
        ret = 0
        while(n):
            ret = (ret << 1) | 1
            n >>= 1
        
        return ret
