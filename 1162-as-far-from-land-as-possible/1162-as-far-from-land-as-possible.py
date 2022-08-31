class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        def nearby(r, c, q):
            for dr, dc in [(1, 0), (0, 1),\
                           (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                q.append((nr, nc))
                
        def bfs():
            nonlocal steps
            while(q):
                steps += 1
                for _ in range(len(q)):
                    x, y = q.popleft()
                
                    if(0 <= x < n and 0 <= y < n\
                       and not grid[x][y]):
                        grid[x][y] = steps
                        nearby(x, y, q)
        
        n = len(grid)
        q = deque()
        steps = 0
        
        for r in range(n):
            for c in range(n):
                if(grid[r][c]):
                    nearby(r, c, q)
        
        bfs()
        return -1 if(steps == 1) else steps - 1
                
                    