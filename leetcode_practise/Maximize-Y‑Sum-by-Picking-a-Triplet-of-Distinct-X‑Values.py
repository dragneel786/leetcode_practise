class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        max_xs = Counter()
        for xv, yv in zip(x, y):
            max_xs[xv] = max(max_xs[xv], yv)
        
        values = sorted(max_xs.values(), reverse=True)[:3]
        return sum(values) if len(values) == 3 else -1
