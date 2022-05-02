class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        rt, ct = 0, cols - 1
        rb, cb = rows - 1, 0
        while(-1 < rt < rows and -1 < ct < cols\
              and -1 < rb < rows and -1 < cb < cols):
            if(matrix[rt][ct] == target or matrix[rb][cb] == target):
                return True
        
            if(matrix[rt][ct] < target):
                rt += 1
            else:
                ct -= 1
            
            if(matrix[rb][cb] > target):
                rb -= 1
            else:
                cb += 1
        
        return False
            