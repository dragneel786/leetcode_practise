class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if(total & 1): return False

        half = total // 2
        dp = [([False] * (half + 1)) for _ in range(n + 1)]

        for x in range(n + 1): dp[x][0] = True

        for i in range(1, n + 1):
            for j in range(1, half + 1):
                dp[i][j] = dp[i - 1][j]
                if(j >= nums[i - 1] and not dp[i][j]):
                    dp[i][j] = dp[i - 1][j - nums[i - 1]]
                
        return dp[n][half]
        
        