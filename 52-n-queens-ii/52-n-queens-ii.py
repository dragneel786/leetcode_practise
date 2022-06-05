class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def placeQueens(r, invalid):
            if(r == n):
                count[0] += 1
                return
            
            for i in range(n):
                if(validate(invalid, [r, i])):
                    invalid[r] = i
                    placeQueens(r + 1, invalid)
                    invalid.pop(r)
        
        def validate(invalid, pos):
            for k in invalid.keys():
                if(k == pos[0] or invalid[k] == pos[1] or\
                  abs(pos[0] - k) == abs(pos[1] - invalid[k])):
                    return False
            return True
        
        count = [0]
        placeQueens(0, dict())
        return count[0]