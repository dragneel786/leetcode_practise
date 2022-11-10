class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        s, e = intervals[0]
        
        for a, b in intervals[1:]:
            if(a <= e or e >= b):
                e = max(e, b)
            else:
                res.append([s, e])
                s, e = a, b
        
        res.append([s, e])
        return res
            
        