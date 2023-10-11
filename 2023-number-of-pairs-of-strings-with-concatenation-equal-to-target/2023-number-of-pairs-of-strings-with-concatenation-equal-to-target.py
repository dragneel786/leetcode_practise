class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counts = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[i + 1:]:
                counts += ((num1 + num2) == target)
                counts += ((num2 + num1) == target)
            
        return counts