from queue import Queue
class Solution:
    def solve(self, board: List[List[str]])-> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if(m < 3 or n < 3):
            return

        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if(board[r][c] == "O"):
                    self.bfs(board, r, c, m, n)
                    
    def bfs(self, board, sr, sc, m, n):
        q = Queue()
        board[sr][sc] = "X"
        visited = [[sr, sc]]
        q.put([sr, sc])
        while(not q.empty()):
            sr, sc = q.get()
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                i, j = sr + di, sc + dj

                if(board[i][j] == "X"):
                    continue

                if(i == m - 1 or j == n - 1 or i == 0 or j == 0):
                    self.revert(board, visited)
                    return

                board[i][j] = "X"
                visited.append([i, j])
                q.put([i, j])

    def revert(self, board, visited):
        for i, j in visited:
            board[i][j] = "O"

