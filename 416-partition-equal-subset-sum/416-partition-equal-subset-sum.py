class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if(total & 1): return False

        half = total // 2
        dp = [True] + ([False] * half)
        
        for i in range(1, n + 1):
            temp = [True] + ([False] * half)
            
            for j in range(1, half + 1):
                temp[j] = dp[j]
                if(j >= nums[i - 1] and not temp[j]):
                    temp[j] = dp[j - nums[i - 1]]
            
            dp = temp[:]
            
        return dp[half]
        
        