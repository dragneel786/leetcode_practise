class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mul = 1
        nums = set(nums)
        while((k * mul) in nums):
            mul += 1
        
        return mul * k
