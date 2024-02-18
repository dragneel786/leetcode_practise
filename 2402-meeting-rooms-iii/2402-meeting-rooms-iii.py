class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meet_count = [0] * n
        free = [i for i in range(n)]
        booked = []
        
        heapify(free) 
        for start, end in sorted(meetings):
            
            while(booked and start >= booked[0][0]):
                _, room = heappop(booked)
                heappush(free, room)
                
            if free:
                room = heappop(free)
                heappush(booked, (end, room))
            else:
                room_available, room = heappop(booked)
                heappush(booked, (room_available + end - start, room))
                
            meet_count[room] += 1
            
        return meet_count.index(max(meet_count))
                
        