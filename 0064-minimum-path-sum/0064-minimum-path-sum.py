class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        @lru_cache(None)
        def min_sum(r, c):
            nonlocal rows, cols
            if(r == rows - 1 and c == cols - 1):
                return grid[r][c]
            
            if(r >= rows or c >= cols):
                return inf
            
            return grid[r][c] + min(min_sum(r + 1, c),\
                                    min_sum(r, c + 1))
        
        rows, cols = len(grid), len(grid[0])
        return min_sum(0, 0)