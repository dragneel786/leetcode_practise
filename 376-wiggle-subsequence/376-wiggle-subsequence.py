class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # [small, large]
        dp = [[1, 1] for _ in range(len(nums))]
        maxW = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if(nums[j] > nums[i]):
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                elif(nums[j] < nums[i]):
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
            
            maxW = max(maxW, max(dp[i]))
        return maxW
                    
                
        