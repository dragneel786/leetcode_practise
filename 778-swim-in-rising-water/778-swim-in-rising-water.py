class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, pq, res, seen = len(grid), [(grid[0][0], 0, 0)], 0, set([(0, 0)])
        while(True):
            m, x, y = heappop(pq)
            res = max(m, res)
            if(x == y == n - 1):
                return res
            
            for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if(0 <= i < n and 0 <= j < n and (i, j) not in seen):
                    seen.add((i, j))
                    heappush(pq, (grid[i][j], i, j))
            
                