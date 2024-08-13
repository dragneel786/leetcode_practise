class Solution:
    def minIncrements(self, n: int, A: List[int]) -> int:
        res = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = i * 2 + 1, i * 2 + 2
            res += abs(A[l] - A[r])
            A[i] += max(A[l], A[r])
        return res
        