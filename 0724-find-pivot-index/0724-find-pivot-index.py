class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        prefix = 0
        
        for i, num in enumerate(nums):
            if(prefix == tot - num):
                return i
            
            prefix += num
            tot -= num
        
        return -1