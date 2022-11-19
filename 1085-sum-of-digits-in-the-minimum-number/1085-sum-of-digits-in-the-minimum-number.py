class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        return ~ sum(map(int, list(str(min(nums))))) & 1