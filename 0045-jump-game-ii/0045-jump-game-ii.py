class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[-1] = 0
        for i in range(n - 2, -1, -1):
            for j in range(i, min(i + nums[i] + 1, n)):
                dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[0]
                
                