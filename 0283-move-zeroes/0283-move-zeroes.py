class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            while(zero_index < len(nums) and nums[zero_index] != 0):
                zero_index += 1
            
            if nums[i] != 0 and zero_index < i:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
        
            