class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        00, 03, 33, 30 | 01, 13, 32, 20 | 02, 23, 31, 10
        11, 12, 22, 21
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n - i - 1],\
                matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] =\
                matrix[n - j - 1][i], matrix[i][j],\
                matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]
                
            
            
