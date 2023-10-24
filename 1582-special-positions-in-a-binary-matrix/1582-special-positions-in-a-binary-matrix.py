class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        cols = [0] * n
        for r in range(m):
            for c in range(n):
                rows[r] += mat[r][c]
                cols[c] += mat[r][c]
        
        return sum([(rows[r] == cols[c] == mat[r][c] == 1)\
                    for r in range(m) for c in range(n)])