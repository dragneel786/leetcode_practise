class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[-1] = 0
        for i in range(n - 2, -1, -1):
            till_idx = i + nums[i] + 1
            dp[i] = min(dp[i: till_idx]) + 1
        
        return dp[0]
                
                