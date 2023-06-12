class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = count = 0
        s += 'OOO'
        has = False
        for c in s:
            has = has or c == 'X'
            count += has
            if(count == 3):
                count = 0
                has = False
                moves += 1
        
        return moves