class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if(m * n != r * c):
            return mat
    
        newMat = [([0] * c) for _ in range(r)]
        k, l = 0, 0
        for i in range(m):
            for j in range(n):
                newMat[l][k] = mat[i][j]
                k += 1
                if(k == c):
                    l += 1
                    k %= c
            
        return newMat