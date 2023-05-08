class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        sums = 0 
        for i in range(size):
            sums += mat[i][i] + mat[i][size - i - 1]
        
        return sums - (mat[size//2][size//2] if(size % 2) else 0)
        