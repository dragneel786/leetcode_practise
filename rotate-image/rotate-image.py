class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n // 2):
            for j in range(n - (i * 2) - 1):
                matrix[i][j + i], matrix[j + i][n - i - 1],\
                matrix[n - i - 1][n - i - 1 - j], matrix[n - i - j - 1][i] =\
                matrix[n - i - j - 1][i], matrix[i][j + i],\
                matrix[j + i][n - i - 1],\
                matrix[n - i - 1][n - i - 1 - j]