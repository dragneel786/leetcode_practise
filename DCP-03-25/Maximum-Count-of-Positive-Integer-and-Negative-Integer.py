class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = pos = 0
        for num in nums:
            neg += (num < 0)
            pos += (num > 0)

        return max(neg, pos)