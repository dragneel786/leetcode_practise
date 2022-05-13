class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        P = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]
        
        def isValid(s):
            for r in range(1, rows - s + 2):
                for c in range(1, cols - s + 2):
                    v = P[r + s - 1][c + s - 1] - P[r-1][c + s - 1]\
                    - P[r + s - 1][c-1] + P[r - 1][c - 1]
                    if(v <= threshold):
                        return True  
            return False
        
        high = min(rows, cols)
        low = 1
        res = 0
        while(low <= high):
            m = (high - low) // 2 + low
            if(isValid(m)):
                res = m
                low = m + 1
            else:
                high = m - 1
        return res
                
                    