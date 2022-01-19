from collections import deque
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_hash = defaultdict(int)
        col_hash = defaultdict(int)
        retry = set()
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col]):
                    row_hash[row] += 1
                    col_hash[col] += 1
                    if(row_hash[row] > 1 and col_hash[col] > 1):
                        total += 1
                    else:
                        retry.add((row, col))

        for r in retry:
            if(row_hash[r[0]] > 1):
                total += 1
            elif(col_hash[r[1]] > 1):
                total += 1
        
        return total