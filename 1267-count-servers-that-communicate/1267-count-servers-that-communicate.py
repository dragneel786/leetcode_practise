from collections import deque
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for row in range(rows):
            for col in range(cols):
                temp = 0
                if(grid[row][col]):
                    temp = self.bfs(grid, row, col)
                    if(temp >= 2):
                        count += temp

        return count

    def bfs(self, grid, row, col):
        count = 1
        q = deque()
        q.append([row, col])
        grid[row][col] = 0
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while(len(q)):
            r, c = q.popleft()
            for d in dir:
                i, j = r + d[0], c + d[1]
                while(i > -1 and j > -1 and i < len(grid) and j < len(grid[0])):
                    if(grid[i][j]):
                        q.append([i, j])
                        grid[i][j] = 0
                        count += 1
                    i, j = i + d[0], j + d[1]
        if(count == 1):
            grid[row][col] = 1

        return count