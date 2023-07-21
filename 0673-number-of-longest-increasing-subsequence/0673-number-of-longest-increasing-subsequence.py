class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1]] * n
        dp[0] = [1, 1]
        largest = 1
        count = 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1): 
                if(nums[i] <= nums[j]):
                    continue

                if(dp[i][0] < dp[j][0] + 1):
                    dp[i] = [dp[j][0] + 1, dp[j][1]]

                elif(dp[i][0] == dp[j][0] + 1):
                    dp[i][1] += dp[j][1]


            if(largest < dp[i][0]):
                largest = dp[i][0]
                count = dp[i][1]

            elif(largest == dp[i][0]):
                count += dp[i][1]

        return count