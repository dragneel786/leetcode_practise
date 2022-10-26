class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum((num for num in sorted(nums)[::2]))