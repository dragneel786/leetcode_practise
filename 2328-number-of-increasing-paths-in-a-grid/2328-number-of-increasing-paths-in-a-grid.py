class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def ways(r, c):
            nonlocal MOD, m, n
            res = 0
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if(0 <= nr < m and 0 <= nc < n \
                   and grid[r][c] < grid[nr][nc]):
                    
                    if(not visited[nr][nc]):
                        visited[nr][nc] = 1 + ways(nr, nc)
                    res = (res + visited[nr][nc]) % MOD
            
            return res
        
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        visited = [([0] * n) for _ in range(m)]
        tot_ways = 0
        for a in range(m):
            for b in range(n):
                if(not visited[a][b]):
                    visited[a][b] = 1 + ways(a, b)
                tot_ways = (tot_ways + visited[a][b]) % MOD
        
        return tot_ways