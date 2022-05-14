class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        res = []

        for r in range(m):
            max_val = max(mat[r])
            max_idx = mat[r].index(max_val)
            res.append([r, max_idx])

        for r, c in res: # just need to verify it is peak in the col too
            if (mat[r-1][c] if r-1>=0 else -1) < mat[r][c] > (mat[r+1][c] if r+1<m else -1):
                return [r, c]