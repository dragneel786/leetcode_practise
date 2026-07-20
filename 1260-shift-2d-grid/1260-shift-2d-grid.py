class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        vals = []
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                vals.append(grid[r][c])
        
        size = rows * cols
        k = size - (k % size)
        vals = vals[k:] + vals[:k]
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = vals[(r * cols) + c]
        
        return grid