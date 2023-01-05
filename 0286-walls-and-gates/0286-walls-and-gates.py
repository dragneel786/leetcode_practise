class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        rows, cols = len(rooms), len(rooms[0])
        for r in range(rows):
            for c in range(cols):
                if(rooms[r][c] == 0):
                    q.append((r, c))
                
        while(q):
            visited = set()
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (0, 1),\
                               (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < rows and 0 <= nc < cols\
                       and rooms[nr][nc] != -1 and\
                       rooms[r][c] + 1 < rooms[nr][nc]):
                    
                        rooms[nr][nc] = rooms[r][c] + 1
                        if((nr, nc) not in visited):
                            q.append((nr, nc))
                            visited.add((nr, nc))
        