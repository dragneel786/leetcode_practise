class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue
                    
                boxIdx = (r // 3) * 3 + (c // 3)
                v = board[r][c]
                if(v in rows[r] or v in cols[c] or v in box[boxIdx]):
                    return False
                
                rows[r].add(v)
                cols[c].add(v)
                box[boxIdx].add(v)
        return True
                