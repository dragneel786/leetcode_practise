class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRow = [0] * n
        maxCol = [0] * n
        for r in range(n):
            for c in range(n):
                maxRow[r] = max(maxRow[r], grid[r][c])
                maxCol[c] = max(maxCol[c], grid[r][c])
            
        total = 0
        for r in range(n):
            for c in range(n):
                inc = min(maxRow[r], maxCol[c])
                if(grid[r][c] < inc):
                    total += (inc - grid[r][c])
        return total