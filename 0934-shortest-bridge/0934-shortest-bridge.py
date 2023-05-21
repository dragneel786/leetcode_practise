class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            nonlocal n
            q.append((r, c))
            grid[r][c] = -1
            for dr, dc in [(-1, 0), (0, -1),\
                           (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if(0 <= nr < n and 0 <= nc < n\
                   and grid[nr][nc] == 1):
                    dfs(nr, nc)
        
        def bfs():
            min_flip = 0
            while(q):
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in [(-1, 0), (0, -1),\
                           (1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if(0 <= nr < n and 0 <= nc < n\
                           and grid[nr][nc] != -1):
                            if(grid[nr][nc] == 1):
                                return min_flip
                            
                            grid[nr][nc] = -1
                            q.append((nr, nc))
                            
                min_flip += 1
                            
                    
                    
        n = len(grid)
        q = deque()
        for a in range(n):
            for b in range(n):
                if(grid[a][b]):
                    dfs(a, b)
                    break
            if(q):
                break
        
        return bfs()