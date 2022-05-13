class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if(r > 0):
                    mat[r][c] += mat[r - 1][c]
                
                if(c > 0):
                    mat[r][c] += mat[r][c - 1]
                
                if(r > 0 and c > 0):
                    mat[r][c] -= mat[r - 1][c - 1]
        
        def isValid(s):
            for r in range(rows - m + 1):
                for c in range(cols - m + 1):
                    v = mat[r + m - 1][c + m - 1]
                    if(r > 0):
                        v -= mat[r - 1][c + m - 1]
                    if(c > 0):
                        v -= mat[r + m - 1][c - 1]
                    if(r > 0 and c > 0):
                        v += mat[r - 1][c - 1]
                        
                    if(v <= threshold):
                        return True  
            return False
        
        high = min(rows, cols)
        low = 0
        res = 0
        while(low <= high):
            m = (high - low) // 2 + low
            if(isValid(m)):
                res = m
                low = m + 1
            else:
                high = m - 1
        
        return res
                
                    