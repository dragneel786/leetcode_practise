class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        first = second = third = -inf
        for num in nums:
            if(first == num or second == num or third == num):
                continue
                
            if(num > first):
                first, second, third = \
                num, first, second
            
            elif(num > second):
                second, third = num, second
            
            elif(num > third):
                third = num
        
        if(third == -inf):
            return first
        
        return third