class NumMatrix:
    prefix = None
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        for c in range(1, cols):
            matrix[0][c] += matrix[0][c - 1]
        for r in range(1, rows):
            matrix[r][0] += matrix[r - 1][0]
        for r in range(1, rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r - 1][c] + matrix[r][c - 1] - matrix[r - 1][c - 1]
        
        self.prefix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        val = self.prefix[row2][col2]
        row1 -= 1
        col1 -= 1
        if(row1 >= 0):
            val -= self.prefix[row1][col2]
        if(col1 >= 0):
            val -= self.prefix[row2][col1]
        if(col1 >=0 and row1 >= 0):
            val += self.prefix[row1][col1]
        
        return val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)