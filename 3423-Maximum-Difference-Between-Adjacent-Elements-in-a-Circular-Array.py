class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        size = len(nums)
        for i in range(size):
            i1 = (i + 1) % size
            max_diff = max(max_diff, abs(nums[i] - nums[i1]))
        
        return max_diff

