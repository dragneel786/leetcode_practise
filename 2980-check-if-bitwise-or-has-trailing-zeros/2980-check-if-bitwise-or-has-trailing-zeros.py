class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        zeros = 0
        for num in nums:
            zeros += (num & 1 == 0)
            if(zeros > 1):
                return True
            
        return False