class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            place = 0
            while(num):
                ret |= (num & 1) << place
                num >>= 1
                place += 1
        
        return ret
            
        