class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        coor_val = {(0,0): grid[0][0]}
        q = [[grid[0][0], 0, 0]]
        while(q):
            obs, sr, sc = heappop(q)
            if sr == rows - 1 and sc == cols - 1:
                return obs

            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = sr + dr, sc + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    state = [obs + grid[nr][nc], nr, nc]
                    coor_val.setdefault((nr,nc), inf)

                    if coor_val[(nr,nc)] > state[0]:
                        coor_val[(nr,nc)] = state[0]
                        heappush(q, state)
        
        
        return res
                            
                        
                
        
        