from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for row in range(rows):
            for col in range(cols):
                if(grid[row][col] == '1'):
                    self.bfs(grid, row, col, rows, cols)
                    count += 1

        return count
    
    def bfs(self, grid, row, col, n1, n2):
        q = Queue()
        q.put((row, col))
        visited = set()
        visited.add((row, col))
        grid[row][col] = '0'
        while(not q.empty()):
            r, c = q.get()
            for i, j in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                if(i > -1 and j > -1 and i < n1 and j < n2 and grid[i][j] == '1' and (i, j) not in visited):
                    grid[i][j] = '0'
                    visited.add((i, j))
                    q.put((i, j))
