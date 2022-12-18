class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        times = 0
        pa, pb = points[0]
        for ca, cb in points[1:]:
            times += max(abs(pa - ca), abs(cb - pb))
            pa, pb = ca, cb
        
        return times
            