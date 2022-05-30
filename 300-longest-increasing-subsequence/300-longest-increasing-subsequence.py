class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        res = -math.inf
        for i in range(n):
            idx = bisect_left(dp, nums[i])
            res = max(idx + 1, res)
            dp[idx] = nums[i]
        return res
        