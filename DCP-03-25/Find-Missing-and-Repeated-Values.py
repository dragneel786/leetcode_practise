class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        values = [0] * (n * n)
        for row in grid:
            for val in row:
                values[val - 1] += 1

        res = [0] * 2
        for i, v in enumerate(values):
            if v == 2:
                res[0] = i + 1

            if v == 0:
                res[1] = i + 1

        return res