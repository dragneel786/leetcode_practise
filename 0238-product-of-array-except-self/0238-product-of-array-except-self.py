class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = 1
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            result[i] = prefix_prod
            prefix_prod *= num
        
        postfix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix_prod
            postfix_prod *= nums[i]
        
        return result
            
        