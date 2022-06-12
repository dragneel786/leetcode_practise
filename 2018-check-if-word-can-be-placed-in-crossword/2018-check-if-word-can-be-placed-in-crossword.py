class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        
        def placed(pos):
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                i = 0
                valid = True
                ro, co = pos
                if(0 <= (ro - dr) < rows \
                   and 0 <= (co - dc) < cols \
                   and board[ro - dr][co - dc] != "#"):
                    continue
                while(0 <= co < cols and 0 <= ro < rows):
                    if(i == n):
                        if(board[ro][co] != "#"):
                            valid = False
                        break
                        
                    if(board[ro][co] != " " and board[ro][co] != word[i]):
                        break
                    ro += dr
                    co += dc
                    i += 1
                if(i == n and valid):
                    return True
            return False
                
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] != "#" and placed([r, c])):
                    return True
        
        return False
        