class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        q = deque([(*entrance, 0)])
        maze[entrance[0]][entrance[1]] = '+'
        rows, cols = len(maze), len(maze[0])
        
        while(q):
            x, y, steps = q.popleft()
            if((x, y) != entrance and (x in [0, rows - 1]\
                                       or y in [0, cols - 1])):
                return steps
                
            for dx, dy in [(1, 0), (0, 1),\
                          (0, -1), (-1, 0)]:
                
                nx, ny = x + dx, y + dy
                if(0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '+'):
                    maze[nx][ny] = '+'
                    q.append((nx, ny, steps + 1))
        
        return -1
        
        
            