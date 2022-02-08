class Solution:
    def addDigits(self, nums: int) -> int:
        def add(n):
            temp = 0
            while(n):
                temp += (n % 10)
                n //= 10
        
            return temp
        
        while(nums > 9):
            nums = add(nums)
        
        return nums