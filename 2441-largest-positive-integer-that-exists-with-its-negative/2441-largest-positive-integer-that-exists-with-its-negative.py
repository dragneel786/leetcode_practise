class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        val = -1
        for num in nums:
            if(num > 0 and -num in nums):
                val = max(num, val)
        
        return val