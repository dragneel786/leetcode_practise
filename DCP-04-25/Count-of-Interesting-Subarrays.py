class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        min_diff = inf
        for i in range(1, len(nums)):
            min_diff = min(min_diff, nums[i] - nums[i - 1])
        
        return min_diff
            