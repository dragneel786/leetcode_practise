"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        res = []
        for i, s in enumerate(schedule):
            heap.append((s[0].start, s[0].end, i, 0))
        
        heapify(heap)
        end = heap[0][1]
        while(heap):
            _, _, i, j = heappop(heap)
            if(len(schedule[i]) > j + 1):
                p = schedule[i][j + 1]
                heappush(heap, (p.start, p.end, i, j + 1))
            
            if(heap):
                if(end < heap[0][0]):
                    res.append(Interval(end, heap[0][0]))
                end = max(end, heap[0][1])
                
        return res