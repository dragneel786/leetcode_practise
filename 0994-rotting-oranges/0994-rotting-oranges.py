class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        q = deque()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        dire = [0,1,0,-1,0]
        mins = 0
        while(q and fresh_count):
            mins += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r + dire[i], c + dire[i + 1]
                    if 0 <= nr < rows and 0 <= nc < cols\
                    and grid[nr][nc] == 1:
                        fresh_count -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            
        
        return -1 if fresh_count != 0 else mins
                        
                    
                