class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([not a == b for a, b in zip(heights,sorted(heights))])