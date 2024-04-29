class Solution:
    def addedInteger(self, n1: List[int], n2: List[int]) -> int:
        return min(n2) - min(n1)