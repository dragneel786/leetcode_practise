class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        start = end = 0
        for i, num in enumerate(nums):
            if(num == 1):
                start = i
            
            if(num == len(nums)):
                end = i
        
        return (start - 0) + (len(nums) - end - 1) - (start > end)
    