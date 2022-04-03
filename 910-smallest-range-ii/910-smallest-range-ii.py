class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        gap = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            mi = min(nums[0] + k, nums[i + 1] - k)
            ma = max(nums[-1] - k, nums[i] + k)
            gap = min(gap, ma - mi)
        
        return gap