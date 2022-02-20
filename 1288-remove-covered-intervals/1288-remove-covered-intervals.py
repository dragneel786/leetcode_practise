class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = list(sorted(intervals, key=lambda x:x[0]))
        seen = set()
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if(intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]):
                    seen.add((intervals[j][0], intervals[j][1]))
                    
                elif(intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]):
                    seen.add((intervals[i][0], intervals[i][1]))

        return len(intervals) - len(seen)