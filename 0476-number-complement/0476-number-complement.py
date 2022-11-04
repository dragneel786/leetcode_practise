class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        step = 0
        while(num):
            res = ((not num & 1) << step) + res
            num >>= 1
            step += 1
        
        return res