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

    def dfs(self, board, word, r, c):
        if(not word):
            return True

        if(r < 0 or c < 0 or r >= len(board) or \
             c >= len(board[0]) or board[r][c] == "_" or board[r][c] != word[0]):
            return False

        temp = board[r][c]
        board[r][c] = "_"
        res = self.dfs(board, word[1:], r + 1, c) or self.dfs(board, word[1:], r, c + 1) or \
                self.dfs(board, word[1:], r - 1, c) or self.dfs(board, word[1:], r, c - 1)
        board[r][c] = temp

        return res