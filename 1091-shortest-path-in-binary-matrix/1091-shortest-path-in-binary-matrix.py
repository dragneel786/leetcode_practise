class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if(grid[0][0] or grid[n - 1][n - 1]):
            return -1
        
        q = deque([(0, 0)])
        grid[0][0] = 1
        steps = 1
        while(q):
            for _ in range(len(q)):
                r, c = q.popleft()
                if(r == c == n - 1):
                    return steps
                
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1),\
                               (1,1),(1,-1),(-1,1),(-1,-1)]:
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < n and 0 <= nc < n\
                       and not grid[nr][nc]):
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            
            steps += 1
        
        return -1
        