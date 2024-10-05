class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def visited(key = 0):
            nonlocal visit_room
            visit_room.add(key)
            for k in rooms[key]:
                if k not in visit_room:
                    visited(k)
        
        visit_room = set([0])
        visited(0)
        # print(visit_room)
        return len(visit_room) == len(rooms)