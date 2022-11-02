class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        max_size = 0
        print(intervals)
        for s, e in intervals:
            while(heap and heap[0] <= s):
                heappop(heap)
            
            heappush(heap, e)
            
            max_size = max(len(heap), max_size)
        
        return max_size