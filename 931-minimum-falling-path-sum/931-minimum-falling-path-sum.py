class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n - 2, -1, -1):
            for j in range(n):
                val = matrix[i][j]
                matrix[i][j] += matrix[i + 1][j]
                for di, dj in [[1, 1], [1, -1]]:
                    if((-1 < i + di < n) and (-1 < j + dj < n)):
                        matrix[i][j] = min(matrix[i][j], val + matrix[i + di][j + dj])
        return min(matrix[0])