class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        ans = [0] * cols
        for r in range(rows):
            for c in range(cols):
                ans[c] = max(ans[c], len(str(grid[r][c])))
        
        return ans