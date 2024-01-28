class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        prev_row = grid[0].copy()
        for r in range(1, rows):
            nxt_row = grid[r].copy()
            for c in range(cols):
                min_ans = inf
                for k in range(cols):
                    min_ans = min(min_ans, grid[r - 1][k] + moveCost[prev_row[k]][c])
        
                grid[r][c] += min_ans
            
            prev_row = nxt_row
            # print(grid[r])
        return min(grid[-1])
            