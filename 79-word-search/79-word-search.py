class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == word[0]):
                    if(self.dfs(board, word, r, c)):
                        return True

        return False

    def dfs(self, board, word, r, c, i = 0):
        if(i == len(word)):
            return True

        if(r < 0 or c < 0 or r >= len(board) or \
             c >= len(board[0]) or board[r][c] == "_" or board[r][c] != word[i]):
            return False

        temp = board[r][c]
        board[r][c] = "_"
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if(self.dfs(board, word, r + di, c + dj, i + 1)):
                return True

        board[r][c] = temp
        return False