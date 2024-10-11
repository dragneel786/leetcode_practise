class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        heap, free_seats = [], []
        times = [[i, a, b] for i, (a, b) in enumerate(times)]
        times.sort(key=lambda a: a[1])
        seat = 0
        for i, start, end in times:
            while(heap and start >= heap[0][0]):
                _, empty = heappop(heap)
                heappush(free_seats, empty)
            
            assigned = -1
            if free_seats:
                s = heappop(free_seats)
                assigned = s
            else:
                assigned = seat
                seat += 1
            
            if i == targetFriend:
                return assigned
            
            heappush(heap, (end, assigned))
            # print(heap, free_seats, seat)
        return -1
            
            
            
            
            
            
            
            
            
        
        
        