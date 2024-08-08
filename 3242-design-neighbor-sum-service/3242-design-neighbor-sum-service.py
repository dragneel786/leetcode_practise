class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.asum = {}
        self.dsum = {}
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                asm = dsm = 0 
                for dr, dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                    nr, nc = r + dr, c + dc
                    if -1 < nr < rows and -1 < nc < cols:
                        asm += grid[nr][nc]
                
                for dr, dc in [[1,1],[1,-1],[-1,1],[-1,-1]]:
                    nr, nc = r + dr, c + dc
                    if -1 < nr < rows and -1 < nc < cols:
                        dsm += grid[nr][nc]
                
                self.asum[grid[r][c]] = asm
                self.dsum[grid[r][c]] = dsm
        
        
    def adjacentSum(self, value: int) -> int:
        return self.asum[value] 

    def diagonalSum(self, value: int) -> int:
        return self.dsum[value]


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)