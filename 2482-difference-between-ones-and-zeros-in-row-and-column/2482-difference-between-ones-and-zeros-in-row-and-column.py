class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        ones_cols = [0] * cols
        ones_rows = [0] * rows
        zeros_cols = [0] * cols
        zeros_rows = [0] * rows
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if(not val):
                    zeros_rows[i] += 1
                    zeros_cols[j] += 1
                
                else:
                    ones_cols[j] += 1
                    ones_rows[i] += 1
        
        res = [([0] * cols) for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res[i][j] = ones_rows[i] + ones_cols[j]\
                - zeros_rows[i] -  zeros_cols[j]
        
        return res
                
    