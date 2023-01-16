class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        left = []
        right = []
        for s, e in intervals:
            if(e < ns):
                left.append([s, e])
            elif(ne < s):
                right.append([s, e])
            else:
                ns = min(ns, s)
                ne = max(ne, e)
        
        return left + [[ns, ne]] + right