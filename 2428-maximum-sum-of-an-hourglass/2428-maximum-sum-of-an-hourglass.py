class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(1, cols):
                grid[r][c] += grid[r][c - 1]
        
        ans = 0
        curr_row = 0
        for row in range(rows - 2):
            for col in range(2, cols):
                row1_sum = grid[row][col]
                row2_sum = grid[row + 2][col]
                if(col > 2):
                    row1_sum -= grid[row][col - 2 - 1]
                    row2_sum -= grid[row + 2][col - 2 - 1]
                
                middle_sum = grid[row + 1][col - 1] - \
                grid[row + 1][col - 2]
                ans = max(row1_sum + row2_sum +\
                          middle_sum, ans)
        
        return ans
                
            