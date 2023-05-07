class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c, direc):
            nonlocal rows, cols
            grid[r][c] = 0
            sign.append(direc)
            
            for dr, dc, ch in [(0, 1, 'r'), (1, 0, 'd'),\
                               (0, -1, 'l'), (-1, 0, 'u')]:
                nr, nc = r + dr, c + dc
                if(0 <= nr < rows and\
                   0 <= nc < cols and\
                   grid[nr][nc]):
                    dfs(nr, nc, ch)
            
            sign.append('|')
            
        
        
        rows, cols = len(grid), len(grid[0])
        iset = set()
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]):
                    sign = []
                    dfs(r, c, '0')
                    iset.add(tuple(sign))
        
        return len(iset)
        
        
                
                
        