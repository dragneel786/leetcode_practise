class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        markC = False
        for r in range(rows):
            for c in range(cols):
                if(not matrix[r][c]):
                    matrix[0][c] = 0
                    if(r == 0):
                        markC = True
                    else:
                        matrix[r][0] = 0
                    
        
        for r in range(1, rows):
            if(not matrix[r][0]):
                matrix[r] = [0] * cols
        
        for c in range(cols):
            if(not matrix[0][c]):
                for i in range(rows):
                    matrix[i][c] = 0
        if(markC):
            for i in range(cols):
                matrix[0][i] = 0
                
                
        
        
        
        
                    
                