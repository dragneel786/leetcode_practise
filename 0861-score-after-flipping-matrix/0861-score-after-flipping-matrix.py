class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # Rows 
        for g in grid:
            if(g[0] == 1):
                continue
            for i, v in enumerate(g):
                g[i] = 0 if(v) else 1
                
        
        rows, cols = len(grid), len(grid[0])
        for c in range(cols):
            one_counts = zero_counts = 0
            for r in range(rows):
                one_counts += grid[r][c] == 1
                zero_counts += grid[r][c] == 0

            if(one_counts > zero_counts):
                continue
            
            for r in range(rows):
                grid[r][c] = 0 if(grid[r][c]) else 1
        
        ans = 0
        for g in grid:
            ans += int(''.join(map(str, g)), 2)
        
        return ans
        
            
        
                