class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sumP = 0
        sumS = 0
        for i in range(n):
            sumP += mat[i][i]
            sumS += mat[i][n - 1 - i]
        
        if(n & 1):
            sumS -= mat[n // 2][n // 2]
        
        return sumS + sumP
        