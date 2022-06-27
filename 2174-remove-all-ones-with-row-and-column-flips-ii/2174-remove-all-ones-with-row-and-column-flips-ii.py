class Solution:
    def removeOnes(self, grid: List[List[int]], mi = 0, mj = 0) -> int:
        res = 16
        ones = 0
        for i in range(len(grid)):
            if((mi & (1 << i)) == 0):
                for j in range(len(grid[0])):
                    if((mj & (1 << j)) == 0 and grid[i][j]):
                        ones += 1
                        res = min(res, 1 + self.removeOnes(grid, mi + (1 << i), mj + (1 << j)))
        return ones if not ones else res
        
        