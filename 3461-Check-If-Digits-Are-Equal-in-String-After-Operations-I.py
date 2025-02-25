class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        up, down, left, right = inf, 0, inf, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    up = min(up, r)
                    down = max(down, r)
                    left = min(left, c)
                    right = max(right, c)
        
        
        return (down - up + 1) * (right - left + 1) * 1