class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 0
        while(res < n):
            res = (res << 1) + 1
        
        return res