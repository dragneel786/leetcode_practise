class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counts = 0
        intervals.sort()
        end = -inf
        for a, b in intervals:
            if(a < end):
                counts += 1
                end = min(b, end)
            else:
                end = b
        
        return counts
                