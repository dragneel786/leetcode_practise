class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps = 0
        for num in nums:
            steps += (num == steps % 2)
        
        return steps