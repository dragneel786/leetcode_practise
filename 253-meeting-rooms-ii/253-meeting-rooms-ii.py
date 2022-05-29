class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [intervals[0][1]]
        rooms = 1
        for i in range(1,len(intervals)):
            if(intervals[i - 1][1] > intervals[i][0]):
                if(heap and heap[0] > intervals[i][0]):
                    rooms += 1
                else:
                    heappop(heap)
            else:
                heappop(heap)
            heappush(heap, intervals[i][1])
        return rooms
    