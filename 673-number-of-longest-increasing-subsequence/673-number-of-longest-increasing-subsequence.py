class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [1, 1]
        maxM = 1
        for i in range(1, n): 
            val = 0
            count = 1
            for j in range(i):
                if(nums[i] > nums[j]):
                    if(dp[j][0] > val):
                        val = dp[j][0]
                        count = dp[j][1]
                    elif(dp[j][0] == val):
                        count += dp[j][1]

            dp[i][0] = val + 1
            dp[i][1] = count
            maxM = max(maxM, dp[i][0])

        count = 0
        for i in range(n):
            if(maxM == dp[i][0]):
                count += dp[i][1]

        # print(dp)
        return count