class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        anti = 0
        dig = 0
        # A = adds and B = subtracts
        for i, m in enumerate(moves):
            x, y = m
            inc = -1 if (i % 2) else 1
            rows[x], cols[y] = rows[x] + inc, cols[y] + inc
            dig += inc if(x == y) else 0
            anti += inc if(x + y == 2) else 0
            if(rows[x] == 3 or cols[y] == 3 or anti == 3 or dig == 3):
                return 'A'
            if(rows[x] == -3 or cols[y] == -3 or anti == -3 or dig == -3):
                return 'B'
            
        if(len(moves) == 9):
            return 'Draw'
        return 'Pending'