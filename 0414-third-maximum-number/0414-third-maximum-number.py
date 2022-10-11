class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        
        if(len(nums) < 3):
            return max(nums)
        
        first = second = third = -inf
        for num in nums:
            if(num > first):
                first, second, third = \
                num, first, second
            
            elif(num > second):
                second, third = num, second
            
            elif(num > third):
                third = num
        
        return third