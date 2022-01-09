class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                dp[i] = min(1 + dp[j], dp[i])

        return dp[0]