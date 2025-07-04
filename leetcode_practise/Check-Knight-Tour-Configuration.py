class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # Base case
        if grid[0][0] != 0:
            return False

        n = len(grid)
        directions = {(-2, 1), (-1, 2), (1, 2), (2, 1),
                      (2, -1), (1, -2), (-1, -2), (-2, -1)}

        path = [None] * (n * n)
        for r in range(n):
            for c in range(n):
                path[grid[r][c]] = (r, c)

        for i in range(1, n * n):
            if (path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1]) not in directions:
                return False
        return True