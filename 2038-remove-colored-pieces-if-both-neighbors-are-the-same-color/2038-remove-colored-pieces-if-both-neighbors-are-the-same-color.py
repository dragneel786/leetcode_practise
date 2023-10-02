class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_moves = b_moves = 0
        curr_a = curr_b = 0
        for c in colors + ('A' if(colors[-1] == 'B') else 'B'):
            if(c == 'A'):
                curr_a += 1
                if(curr_b):
                    b_moves += max(curr_b - 2, 0)
                curr_b = 0
            else:
                curr_b += 1
                if(curr_a):
                    a_moves += max(curr_a - 2, 0)
                curr_a = 0
        
            # print(a_moves, b_moves)
        return a_moves > b_moves