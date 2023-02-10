class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        
        def bfs(q):
            nonlocal rows, cols
            max_dis = 0
            while(q):
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        
                        nr, nc = (r + dr), (c + dc)
                        if(0 <= nr < rows and 0 <= nc < cols\
                           and not grid[nr][nc]):
                            grid[nr][nc] = max_dis + 1
                            q.append((nr, nc))
                 
                if(q):
                    max_dis += 1
            return max_dis
        
        
        
        q = deque()
        comap = dict()
        counter = 1
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):    
                if(grid[r][c] == 1):
                    q.append((r, c))
                
        ret = bfs(q)
        return ret if(ret) else -1
                    
                    