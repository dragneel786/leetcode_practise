class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        sr, sc = 0, n - 1
        for i in range((n * 2) - 1):
            curr = []
            nr, nc = sr, sc
            while(0 <= nr < n and 0 <= nc < n):
                curr.append(grid[nr][nc])
                nr += 1
                nc += 1
            
            curr.sort(reverse=sc==0)
            nr, nc = sr, sc
            for v in curr:
                grid[nr][nc] = v
                nr += 1
                nc += 1
            
            sr += sc == 0
            sc -= sc != 0
            
        return grid

