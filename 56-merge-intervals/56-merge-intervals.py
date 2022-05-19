class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        n = len(intervals)
        while(i < len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            j = i + 1
            while(j < n and end >= intervals[j][0]):
                end = max(end, intervals[j][1])
                j += 1
            
            res.append([start, end])
            if(j == n):
                break
            i = j
        
        return res