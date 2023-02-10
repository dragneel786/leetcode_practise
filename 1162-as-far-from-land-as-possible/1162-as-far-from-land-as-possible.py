class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        
        def bfs(q):
            nonlocal rows, cols
            ans = -1
            while(q):
                for _ in range(len(q)):
                    key, r, c = q.popleft()
                    ans = max(ans, grid[r][c])
                    
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1),\
                                  (-1, 1), (1, -1), (-1, -1), (1, 1)]:
                        
                        nr, nc = (r + dr), (c + dc)
                        kr, kc = comap[key]
                        md = abs(kr - nr) + abs(kc - nc)
                        
                        if(0 <= nr < rows and 0 <= nc < cols\
                           and grid[nr][nc] > md):
                            grid[nr][nc] = md
                            q.append((key, nr, nc))
            return ans
        
        
        
        q = deque()
        comap = dict()
        counter = 1
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):    
                if(grid[r][c] == 1):
                    grid[r][c] = -1
                    comap[counter] = (r, c)
                    q.append((counter, r, c))
                else:
                    grid[r][c] = 3000
                counter += 1
                

        return bfs(q)
                    
                    