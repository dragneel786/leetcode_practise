class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            maxV = 0
            for j in range(i):
                if(nums[i] > nums[j]):
                    maxV = max(maxV, dp[j])
            dp[i] = maxV + 1
        
        return max(dp)
        