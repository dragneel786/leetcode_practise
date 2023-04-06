class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def is_closed(r, c):
            closed = True
            q = deque([(r, c)])
            
            while(q):
                r, c = q.popleft()
                grid[r][c] = 1
                
                for dr, dc in [(0,1), (1,0),\
                               (-1,0), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if(0 > nr or nr >= rows or\
                       nc < 0 or nc >= cols):
                        closed = False
                        continue
                    
                    if(not grid[nr][nc]):
                        q.append((nr, nc))
            
            
            return closed
                       
                       
                       
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if(not grid[r][c]):
                    ans += is_closed(r, c)
        
        return ans