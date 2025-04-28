class Solution:
    def taskSchedulerII(self, A: List[int], space: int) -> int:
        last = defaultdict(lambda: - len(A) - 10)
        res = 0
        for a in A:
            last[a] = res = max(res, last[a] + space) + 1
        return res



