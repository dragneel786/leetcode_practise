class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        res, n = 0, len(nums)
        for i in range(n - 1):
            res += nums[n - 1] - nums[i]
        
        return res
