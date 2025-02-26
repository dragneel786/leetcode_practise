class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = mins = maxs = 0
        for num in nums:
            s += num
            mins = min(mins, s)
            maxs = max(maxs, s)
        
        return maxs - mins