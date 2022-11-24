class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        for e, num in enumerate(nums):
            while(even < len(nums) and nums[even] % 2 == 0):
                even += 2
            
            if(e % 2 == 1 and num % 2 == 0):
                nums[even], nums[e] = nums[e], nums[even]
        
        return nums
            
            
            
            
            
            