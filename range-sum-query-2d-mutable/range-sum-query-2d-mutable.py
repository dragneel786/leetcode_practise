class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.original = [m[:] for m in matrix]
        self.mat = matrix
        self.updateWith(0, 0)
        

    def update(self, row: int, col: int, val: int) -> None:
        self.original[row][col] = val 
        self.updateWith(row, col)
     
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret_val = self.mat[row2][col2]
        if(row1 > 0):
            ret_val -= self.mat[row1 - 1][col2]
        
        if(col1 > 0):
            ret_val -= self.mat[row2][col1 - 1]
        
        if(row1 > 0 and col1 > 0):
            ret_val += self.mat[row1 - 1][col1 - 1]
        
        return ret_val
    
    def updateWith(self, start_row, start_col):
        matrix = self.mat
        m, n = len(matrix), len(matrix[0])
        for r in range(start_row, m):
            for c in range(start_col, n):
                
                val = self.original[r][c]
                if(r > 0):
                    val += matrix[r - 1][c]
                
                if(c > 0):
                    val += matrix[r][c - 1]
                
                if(r > 0 and c > 0):
                    val -= matrix[r - 1][c - 1]
                
                matrix[r][c] = val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)