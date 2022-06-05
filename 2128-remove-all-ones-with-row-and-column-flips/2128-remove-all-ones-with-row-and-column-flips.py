class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(cols):
            if(grid[0][i]):
                for j in range(rows):
                    grid[j][i] = 1 ^ grid[j][i]
        
        for i in range(1, rows):
            val = sum(grid[i])
            if(val != 0 and val != cols):
                return False
        return True
        
        