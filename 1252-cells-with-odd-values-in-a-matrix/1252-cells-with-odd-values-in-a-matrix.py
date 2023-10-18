class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        
        odds = 0
        for r in range(m):
            for c in range(n):
                if((rows[r] + cols[c]) % 2):
                    odds += 1
        
        return odds