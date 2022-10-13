class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_till = nums[0]
        
        for num in nums[1:]:
            max_till = max(max_till + num, num)
            max_so_far = max(max_so_far, max_till)
        
        return max_so_far