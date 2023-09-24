class Solution:
    def minOperations(self, n: int) -> int:
        return sum([n - v for v in range(1, n, 2)])