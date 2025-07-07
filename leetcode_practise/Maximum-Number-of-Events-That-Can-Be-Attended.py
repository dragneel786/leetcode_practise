class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        max_day = max(e for _, e in events)
        heap = []
        ans = j = 0
        for i in range(1, max_day + 1):
            while(j < len(events) and events[j][0] <= i):
                heappush(heap, events[j][1])
                j += 1
            
            while(heap and heap[0] < i):
                heappop(heap)
            
            if heap:
                heappop(heap)
                ans += 1
        
        return ans

        

