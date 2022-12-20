class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        opened = {0}
        q = deque([0])
        
        while(q):
            node = q.popleft()
            for v in rooms[node]:
                if(v not in opened):
                    opened.add(v)
                    q.append(v)
        
        return len(opened) == n
        
        