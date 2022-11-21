class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r, c = entrance
        q = deque([(r, c, 0)])
        maze[r][c] = '+'
        
        rows, cols = len(maze), len(maze[0])
        
        while(q):
            x, y, steps = q.popleft()
            
            for dx, dy in [(1, 0), (0, 1),\
                          (0, -1), (-1, 0)]:
                
                nx, ny = x + dx, y + dy
                if(0 <= nx < rows and 0 <= ny < cols\
                   and maze[nx][ny] != '+'):
                    
                    if(nx == 0 or nx == rows - 1 or\
                       ny == 0 or ny == cols - 1):
                        return steps + 1
                    
                    maze[nx][ny] = '+'
                    q.append((nx, ny, steps + 1))
        
        return -1
        
        
            