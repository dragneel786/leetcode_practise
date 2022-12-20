class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        closed_rooms = {i for i in range(1, n)}
        q = deque([0])
        
        while(q):
            node = q.popleft()
            for v in rooms[node]:
                if(v in closed_rooms):
                    closed_rooms.remove(v)
                    q.append(v)
        
        return len(closed_rooms) == 0
        
        