class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        bit_or = 0
        for num in nums:
            if num % 2 == 0:
                bit_or |= num
        
        return bit_or