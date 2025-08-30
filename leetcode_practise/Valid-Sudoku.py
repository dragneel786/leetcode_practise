class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                
                bi = ((r // 3) * 3) + (c // 3)
                if v in rows[r] or v in cols[c] or v in boxes[bi]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                boxes[bi].add(v)
        
        return True




