class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        sums = 0 
        for i in range(size):
            if(size % 2 == 0 or i != (size // 2)):
                sums += mat[i][i]
            sums += mat[i][size - i - 1]
        
        return sums
        