class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(2)
        zero_idx = -1
        for i in range(len(nums) - 1):
            nums[abs(nums[i])] *= -1
            if(nums[i] == 0):
                zero_idx = i
        
        if(zero_idx == -1):
            return 0
        
        for i in range(len(nums)):
            if(nums[i] > 0):
                return i
            
        return zero_idx
        
        