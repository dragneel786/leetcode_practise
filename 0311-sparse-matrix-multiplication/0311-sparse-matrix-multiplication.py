class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1, c1 = len(mat1), len(mat1[0])
        r2, c2 = len(mat2), len(mat2[0])
        ans = [([0] * c2) for _ in range(r1)]
        for i in range(r1):
            for k in range(c1):
                if(mat1[i][k]):
                    for j in range(c2):
                        ans[i][j] += (mat1[i][k] * mat2[k][j])
        
        return ans