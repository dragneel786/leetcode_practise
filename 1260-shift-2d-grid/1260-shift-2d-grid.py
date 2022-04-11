class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        tot = rows * cols
        k = k % tot
        for _ in range(k):
            i = tot - 2
            temp = grid[rows - 1][cols - 1]
            while(i > -1):
                grid[(i + 1) // cols][(i + 1) % cols] = grid[i // cols][i % cols]
                i -= 1
            grid[(i + 1) // cols][(i + 1) % cols] = temp
        return grid