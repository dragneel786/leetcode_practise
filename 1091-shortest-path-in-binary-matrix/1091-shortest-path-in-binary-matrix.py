from queue import Queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if(grid[0][0] or grid[n - 1][n - 1]):
            return -1

        q = Queue()
        path = 0
        q.put((0, 0))
        q.put((-1, -1))
        grid[0][0] = 1
        while(not q.empty()):
            r, c = q.get()
            if(r == n - 1 and c == n - 1):
                return path + 1

            if(r == -1 and c == -1):
                path += 1
                if(not q.empty()):
                    q.put((-1, -1))   
                continue

            for i, j in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)\
                , (r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1)):

                if(i > -1 and j > -1 and i < n and j < n and not grid[i][j]):
                    grid[i][j] = 1
                    q.put((i, j))

        return -1