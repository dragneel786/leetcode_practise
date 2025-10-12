class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        tot, mul = 0, 1
        for num in nums:
            tot += (num * mul)
            mul *= -1
        
        return tot