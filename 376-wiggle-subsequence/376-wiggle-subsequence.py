class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if(len(nums) < 2): return len(nums)
        sign = 0
        lens = 1
        for i in range(1, len(nums)):
            if(nums[i - 1] < nums[i] and sign != -1):
                lens += 1
                sign = -1
            elif(nums[i - 1] > nums[i] and sign != 1):
                lens += 1
                sign = 1
        return lens
                
                    
                
        