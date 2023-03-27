class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        val = lambda x, y: grid[x][y] \
        if(x < rows and y < cols) else inf
        rows, cols = len(grid), len(grid[0])
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if(r == rows - 1 and c == cols - 1):
                    continue
                    
                grid[r][c] += min(val(r + 1, c),\
                                 val(r, c + 1))
        
        return grid[0][0]
                
                           
        