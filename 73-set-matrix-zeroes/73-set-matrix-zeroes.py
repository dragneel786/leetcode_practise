class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zeroRow, zeroCol = False, False
        for r in range(rows):
            for c in range(cols):
                if(not matrix[r][c]):
                    if(c != 0):
                        matrix[0][c] = 0
                    else:
                        zeroRow = True
                    if(r != 0):
                        matrix[r][0] = 0
                    else:
                        zeroCol = True
                    
        
        for r in range(1, rows):
            if(not matrix[r][0]):
                matrix[r] = [0] * cols
        
        for c in range(cols):
            if(not matrix[0][c]):
                for i in range(rows):
                    matrix[i][c] = 0
        
        if(zeroRow):
            for i in range(rows):
                matrix[i][0] = 0
        
        if(zeroCol):
            for i in range(cols):
                matrix[0][i] = 0
                
                
        
        
        
        
                    
                