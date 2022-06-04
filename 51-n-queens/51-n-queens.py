class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def placeQueens(r, board, invalid = dict()):
            if(r == n):
                res.append(board.copy())
                return

            for i in range(n):
                if(posRight(invalid, [r, i])):
                    board[r] = ("." * i) + 'Q' + ("." * (n - i - 1))
                    invalid[r] = i
                    placeQueens(r + 1, board, invalid)
                    invalid.pop(r)
                    board[r] = "." * n

        def posRight(invalid, pos):
            for k in invalid.keys():
                if(pos[0] == k or pos[1] == invalid[k] or \
                    abs(pos[0] - k) == abs(pos[1] - invalid[k])):
                    return False
            return True

        res = []
        board = [ ("." * n) for _ in range(n)]
        placeQueens(0, board)
        return res