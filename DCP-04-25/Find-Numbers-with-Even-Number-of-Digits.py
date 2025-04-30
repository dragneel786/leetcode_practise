class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counts = 0
        for num in nums:
            digit_cnts = 0
            while(num > 0):
                digit_cnts += 1
                num //= 10
            
            counts += (digit_cnts % 2 == 0)
        
        return counts