class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        minr = [inf] * rows
        maxc = [-inf] * cols
        for r in range(rows):
            for c in range(cols):
                val = matrix[r][c]
                minr[r] = min(val, minr[r])
                maxc[c] = max(val, maxc[c])
        
        ans = []
        for a, b in product(minr, maxc):
            if(a == b):
                ans.append(b)
        
        return ans