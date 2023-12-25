class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        grid = [([0] * cols) for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                min_val = min(rowSum[r], colSum[c])
                rowSum[r] -= min_val
                colSum[c] -= min_val
                grid[r][c] = min_val
        
        return grid
        