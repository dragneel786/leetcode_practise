class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if r - 1 > -1:
                    grid[r][c] += grid[r - 1][c]

                if c - 1 > -1:
                    grid[r][c] += grid[r][c - 1]

                if r - 1  > -1 and c - 1 > -1:
                    grid[r][c] -= grid[r - 1][c - 1]

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > k:
                    break

                count += 1

        return count 

    