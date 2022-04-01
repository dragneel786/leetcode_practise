class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i > 0):
                    matrix[i][j] += matrix[i - 1][j]
                
                if(j > 0):
                    matrix[i][j] += matrix[i][j - 1]

                if(i > 0 and j > 0):
                    matrix[i][j] -= matrix[i - 1][j - 1]
                    
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = self.matrix[row2][col2]
        if(row1 > 0):
            val -= self.matrix[row1 - 1][col2]
        
        if(col1 > 0):
            val -= self.matrix[row2][col1 - 1]
        
        if(row1 > 0 and col1 > 0):
            val += self.matrix[row1 - 1][col1 - 1]

        return val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)