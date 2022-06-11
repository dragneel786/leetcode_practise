class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if(nums[0] > x < nums[-1]):
            return -1
        
        n = len(nums)
        find = sum(nums) - x
        maxL, sub, j = (-math.inf, 0, 0)
        for i in range(n):
            sub += nums[i]
            while(j <= i and sub > find):
                sub -= nums[j]
                j += 1
            
            if(sub == find):
                maxL = max(maxL, i - j + 1)
        
        if(maxL == -math.inf):
            return -1
        
        return n - maxL
            
            
        
        
        