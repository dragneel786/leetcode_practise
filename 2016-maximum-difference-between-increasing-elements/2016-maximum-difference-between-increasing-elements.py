class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxs = [0] * n
        maxs[-1] = nums[-1]
    
        for i in range(n - 2, -1, -1):
            maxs[i] = max(nums[i], maxs[i + 1])
        
        maxd = -1
        minv = nums[0]
        for i in range(1, n):
            minv = min(nums[i], minv)
            if(minv < maxs[i]):
                maxd = max(maxd, maxs[i] - minv)
        
        return maxd