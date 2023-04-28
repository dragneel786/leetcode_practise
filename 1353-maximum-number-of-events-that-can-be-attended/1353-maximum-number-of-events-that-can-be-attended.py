class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        heap = []
        res = d = 0
        while(events or heap):
            if(not heap): d = events[-1][0]
            while(events and events[-1][0] <= d):
                heappush(heap, events.pop()[1])
            
            heappop(heap)
            res += 1
            d += 1
            while(heap and heap[0] < d):
                heappop(heap)
        
        return res
                

                
        