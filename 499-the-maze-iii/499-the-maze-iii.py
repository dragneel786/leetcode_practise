class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # Do BFS for shortest distance
        # Start from the pos and store the state as (direction{l,r,u,d}, pos, distance)
        # keep moving in the same direction until you can't.
        # And then move in all the possible direction.
        # Also keep storing the visited cell if once again gone to the same cell just remove that element.
        # if the hole comes in between return baby.
        dire = {"l":(0, -1), "r":(0, 1), "u":(-1, 0), "d":(1, 0)}
        
        m, n = len(maze), len(maze[0])
        state = (0, "$", tuple(ball))
        heap = [state]
        visited = set()
        while(heap):
            dis, dirc, (x, y) = heappop(heap)
            if((x, y) == tuple(hole)):
                return dirc[1:]
            
            dx, dy = dire.get(dirc[-1], (0, 0))
            nx, ny = x + dx, y + dy
            if(dirc == "$" or nx < 0 or nx >= m or\
               ny < 0 or ny >= n or maze[nx][ny]):
                visited.add((x, y))
                for di, (dx, dy) in dire.items():
                    nx, ny = x + dx, y + dy
                    if(0 <= nx < m and 0 <= ny < n and\
                       not maze[nx][ny] and (nx, ny) not in visited):
                        newState = (dis + 1, dirc + di, (nx, ny))
                        heappush(heap, newState)
                        
            elif((nx, ny) not in visited):
                newState = (dis + 1, dirc, (nx, ny))
                heappush(heap, newState)
        
        return "impossible"
                
                