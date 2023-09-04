class Solution:
    def averageValue(self, nums: List[int]) -> int:
        values = [num for num in nums if num % 3 == num % 2 == 0]
        return sum(values) // len(values) if values else 0