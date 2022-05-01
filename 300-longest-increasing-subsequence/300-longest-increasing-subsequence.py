class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * (n + 1)
        dp[0] = -math.inf
        maxi = 1
        for i in range(n):
            idx = bisect_right(dp, nums[i])
            if(dp[idx - 1] < nums[i]):
                maxi = max(maxi, idx)
                dp[idx] = nums[i]

        return maxi
        