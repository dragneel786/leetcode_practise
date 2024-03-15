class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1
        for num in nums:
            if(not num):
                zeros += 1
            else:
                prod *= num
                
            if(zeros > 1):
                return [0] * len(nums)
            
            
        
        for i, num in enumerate(nums):
            if(zeros):
                if(not num):
                    nums[i] = prod
                else:
                    nums[i] = 0
            
            else:   
                nums[i] = prod // num
        
        return nums