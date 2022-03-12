class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if(n == 1):
        #     return
        
        zero = 0
        for i in range(n):
            while(zero < n and nums[zero]):
                zero += 1
            
            if(i > zero and nums[i]):
                nums[zero], nums[i] = nums[i], nums[zero]