class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        
        def dfs(r, c, visited):
            nonlocal valid_pos, rows, cols
            if(grid[r][c] == 2):
                return len(visited) == valid_pos
            
            count = 0
            for dr, dc in [(1, 0), (0, 1),\
                           (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if(0 <= nr < rows and 0 <= nc < cols and\
                   (nr, nc) not in visited and grid[nr][nc] != -1):
                    visited.add((nr, nc))
                    count += dfs(nr, nc, visited)
                    visited.discard((nr, nc))
            
            return count
                
            
        rows, cols = len(grid), len(grid[0])
        valid_pos = 0
        sr = sc = -1
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] != -1):
                    valid_pos += 1
                    if(grid[r][c] == 1):
                        sr, sc = r, c
        
        
        return dfs(sr, sc, set([(sr, sc)]))
                
                    
                