class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            maxTill = 0
            for j in range(i):
                if(nums[j] + 1 != nums[i]):
                    maxTill = max(dp[j], maxTill)

            dp[i] = maxTill + nums[i]

        return max(dp)