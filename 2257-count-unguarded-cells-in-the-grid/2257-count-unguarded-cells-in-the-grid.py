class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 3
        
        for r, c in guards:
            grid[r][c] = 2
        
        
        for gr, gc in guards:
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = gr + dr, gc + dc
                while(0 <= nr < m and\
                      0 <= nc < n and\
                      grid[nr][nc] != 3 and\
                      grid[nr][nc] != 2):
                    
                    grid[nr][nc] = 1
                    nr += dr
                    nc += dc
        
        counts = 0
        for r in range(m):
            for c in range(n):
                counts += grid[r][c] == 0
        
        
        return counts
        
                    