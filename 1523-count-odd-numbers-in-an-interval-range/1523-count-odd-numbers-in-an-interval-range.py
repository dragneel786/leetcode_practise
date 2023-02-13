class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + \
    (low & 1 == 1 and high & 1 == 1)