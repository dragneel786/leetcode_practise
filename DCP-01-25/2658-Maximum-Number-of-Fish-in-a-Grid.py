class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(sr, sc):
            tot = 0
            q = deque([(sr, sc)])
            while(q):
                r, c = q.popleft()
                tot += grid[r][c]
                grid[r][c] = 0
                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                        q.append((nr, nc))
            
            return tot
        
        max_fish = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    max_fish = max(max_fish, bfs(row, col))
        
        return max_fish