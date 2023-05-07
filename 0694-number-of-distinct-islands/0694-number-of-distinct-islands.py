class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            nonlocal rows, cols
            grid[r][c] = 0
            ret = []
            for dr, dc, ch in [(0, 1, 'r'), (1, 0, 'l'),\
                               (0, -1, 'u'), (-1, 0, 'd')]:
                nr, nc = r + dr, c + dc
                if(0 <= nr < rows and\
                   0 <= nc < cols and\
                   grid[nr][nc]):
                    ret.append(ch + dfs(nr, nc))
            
            return '|'.join(ret) + '|'
        
        
        rows, cols = len(grid), len(grid[0])
        iset = set()
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]):
                    island = 'c' + dfs(r, c)
                    iset.add(island)
        
        return len(iset)
        
        
                
                
        