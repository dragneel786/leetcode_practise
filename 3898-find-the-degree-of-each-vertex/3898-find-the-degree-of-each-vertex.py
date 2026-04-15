class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        res = [0] * n
        for i in range(n):
            for j in range(n):
                res[i] += matrix[i][j]
        
        return res
