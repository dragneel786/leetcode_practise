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
            rows[x] += inc
            cols[y] += inc
            if(x == y):
                dig += inc
            if((x, y) in [(2, 0), (0, 2), (1, 1)]):
                anti += inc
            
        if(3 in rows or 3 in cols or anti == 3 or dig == 3):
            return 'A'
        if(-3 in rows or -3 in cols or anti == -3 or dig == -3):
            return 'B'
        if(len(moves) == 9):
            return 'Draw'
        return 'Pending'