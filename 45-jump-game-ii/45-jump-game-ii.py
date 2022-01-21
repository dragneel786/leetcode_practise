class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]