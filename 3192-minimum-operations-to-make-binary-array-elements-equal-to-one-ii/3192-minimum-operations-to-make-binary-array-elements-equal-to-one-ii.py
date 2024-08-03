class Solution:
    def minOperations(self, A: List[int]) -> int:
        res = 0
        for a in A:
            if a == res & 1:
                res += 1
        return res