class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        checkGreater = True
        for i in range(1, len(nums)):
            if((checkGreater and nums[i - 1] > nums[i]) or\
              (not checkGreater and nums[i - 1] < nums[i])):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
            
            checkGreater = not checkGreater
            
        
            
            