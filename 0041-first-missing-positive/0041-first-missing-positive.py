class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if(nums[i] <= 0):
                nums[i] = n + 1
                
        for num in nums:
            idx = abs(num) - 1
            if(idx >= n or nums[idx] < 0):
                continue
            
            nums[idx] *= -1
                
        for i in range(n):
            if(nums[i] > 0):
                return i + 1
        
        return n + 1
                
                