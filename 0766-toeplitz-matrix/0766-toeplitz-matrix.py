class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        r = c = 0
        for a in range(max(rows, cols)):
            r = a
            c = a
            for i in range(1, min(rows, cols)):
                if(r + i < rows and\
                   matrix[r + i][i] != matrix[r][0]):
                    return False
                
                if(c + i < cols and\
                   matrix[i][c + i] != matrix[0][c]):
                    return False
            
        return True
                
            