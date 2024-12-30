class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        for c in range(len(grid[0])):
            prev = grid[0][c]
            for r in range(1, len(grid)):
                res += max(0, prev - grid[r][c] + 1)
                prev = max(prev + 1, grid[r][c])
        
        return res