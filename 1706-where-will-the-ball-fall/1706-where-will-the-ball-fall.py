class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        res = []
        
        for c in range(cols):
            x, y = 0, c
            while(x != rows):
                val = grid[x][y]
                y += val
                if(y < 0 or y == cols or\
                   grid[x][y - val] != grid[x][y]):
                    res.append(-1)
                    break
                
                x += 1
            else:
                res.append(y)
        
        return res
        
            