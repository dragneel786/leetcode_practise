class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        prefix = 0
        
        for i, num in enumerate(nums):
            tot -= num
            if(prefix == tot):
                return i
            prefix += num
            
        
        return -1