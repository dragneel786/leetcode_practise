class Solution:
    def minOperations(self, n: int) -> int:
        return sum(range(n - 1, -1, -2))