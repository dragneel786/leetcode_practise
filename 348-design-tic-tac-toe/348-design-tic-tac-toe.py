class TicTacToe:

    def __init__(self, n: int):
        self.rows, self.cols = [0] * n , [0] * n
        self.dg = self.ag = 0
        self.n = n
        self.gameOver = 0

    def move(self, row: int, col: int, player: int) -> int:
        if(not self.gameOver):
            m, n = 1 if(player == 1) else -1, self.n
            self.rows[row] += m
            self.cols[col] += m
            if(row == col): self.dg += m
            if(row + col == n - 1): self.ag += m
            if(abs(self.rows[row]) == n or abs(self.cols[col]) == n\
               or abs(self.dg) == n or abs(self.ag) == n):
                self.gameOver = player
        return self.gameOver
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)