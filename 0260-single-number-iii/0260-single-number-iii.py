class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = reduce(lambda a, b: a ^ b, nums)
        diff &= -diff
        
        val1 = val2 = 0
        for num in nums:
            if(num & diff > 0):
                val1 ^= num
            else:
                val2 ^= num
        
        return [val1, val2]