class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_board = defaultdict(set)
        k = 0
        for r in range(len(board)):
            if(r and r % 3 == 0):
                k += 3
            for c in range(len(board[0])):
                val = board[r][c]
                if(val != '.'):
                    for st in ['r' + str(r), 'c' + str(c),\
                               str((r//3) * 3 + (c//3))]:
                        
                        if(val in hash_board[st]):
                            return False

                        hash_board[st].add(val)
        
        return True
                
                
        