class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        res = []
        
        for c in range(cols):
            x, y = 0, c
            while(x != rows):
                val = grid[x][y]
                if(val == 1 and (y == cols - 1 or grid[x][y + val] == -1)):
                    res.append(-1)
                    break
                
                if(val == -1 and (y == 0 or grid[x][y + val] == 1)):
                    res.append(-1)
                    break
                
                x += 1
                y += val
            else:
                res.append(y)
        
        return res
        
            