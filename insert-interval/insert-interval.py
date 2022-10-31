class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if(not intervals): return [newInterval]
        
        left, right = [], []
        n = len(intervals)
        new_start, new_end = newInterval
        start = end = -1
        
        for i, (start, end) in enumerate(intervals):
            if(end < new_start):
                left.append(intervals[i])
            
            elif(start > new_end):
                right.append(intervals[i])
                
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        
        return left + [[new_start, new_end]] + right
           