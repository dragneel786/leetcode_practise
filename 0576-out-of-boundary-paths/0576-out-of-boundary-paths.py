class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def find(sr, sc, remain_move):
            nonlocal m, n, MOD
            if(sr < 0 or sr >= m or sc < 0 or sc >= n):
                return 1
            
            if(remain_move < 1):
                return 0
            
            paths = 0
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = sr + dr, sc + dc
                paths = (paths + find(nr, nc, remain_move - 1)) % MOD
            
            return paths
                
        
        MOD = (10 ** 9) + 7
        return find(startRow, startColumn, maxMove)
            