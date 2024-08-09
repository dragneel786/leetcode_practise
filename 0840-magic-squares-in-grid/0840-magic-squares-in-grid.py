class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def helper(sr, sc):
            row_sum = [0] * 3
            col_sum = [0] * 3
            dig = [0, 0]
            seen = set()
            for dr in range(3):
                for dc in range(3):
                    nr, nc = r + dr, c + dc
                    if grid[nr][nc] > 9 or grid[nr][nc] < 1 \
                    or grid[nr][nc] in seen:
                        return False
                    
                    row_sum[dr] += grid[nr][nc]
                    col_sum[dc] += grid[nr][nc]
                    seen.add(grid[nr][nc])
            
            d = 0
            for dr, dc in [[1,1], [1,-1]]:
                for _ in range(3):
                    nr, nc = sr + dr, sc + dc
                    dig[d] += grid[nr][nc]
                
                d += 1
                sc = sc + 2
            print(row_sum, col_sum, dig)
            return len(set(row_sum) | set(col_sum) | set(dig)) == 1
                
        
        res = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows - 2):
            for c in range(cols - 2):
                res += helper(r, c)
        
        return res