class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        rc_map = defaultdict(list)
        
        row_vals = Counter()
        col_vals = Counter()

        for r in range(rows):
            for c in range(cols):
                rc_map[mat[r][c]] = [r, c]
                row_vals[r] += 1
                col_vals[c] += 1
        
        for i, v in enumerate(arr):
            r, c = rc_map[v]
            row_vals[r] -= 1
            col_vals[c] -= 1
            if row_vals[r] == 0 or col_vals[c] == 0:
                return i
        
        return -1
