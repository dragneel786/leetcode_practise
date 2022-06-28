class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            last = -1
            n = len(intervals)
            res = []
            for i, v in enumerate(intervals):
                if(last == -1 and newInterval[1] < v[0]):
                    res.append(newInterval)
                    res.append(v)
                    last = newInterval[1]
                elif(last == -1 and newInterval[0] <= v[1]):
                    last = max(v[1], newInterval[1])
                    res.append([min(newInterval[0], v[0]), last])
                elif(last >= v[0]):
                    last = max(v[1], last)
                    res[-1][1] = last
                else:
                    res.append(v)
            
            if(last == -1):
                res.append(newInterval)
            return res
                    