class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        step = 0
        while(num):
            end = 0 if(num & 1) else 1
            num >>= 1
            res = (end << step) + res
            step += 1
        
        return res