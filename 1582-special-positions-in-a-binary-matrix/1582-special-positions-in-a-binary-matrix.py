class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row_count, col_count = [0] * rows, [0] * cols
        for i in range(rows):
            for j in range(cols):
                row_count[i] += mat[i][j]
                col_count[j] += mat[i][j]
        
        counts = 0
        for i in range(rows):
            for j in range(cols):
                if(mat[i][j] == row_count[i] == col_count[j] == 1):
                    counts += 1
        
        return counts