class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def placeQueens(r, invalid):
            if(r == n):
                count[0] += 1
                return
            
            for i in range(n):
                if(validate(invalid, [r, i])):
                    # invalid[r] = i
                    placeQueens(r + 1, invalid + [(r, i)])
                    # invalid.pop(r)
        
        def validate(invalid, pos):
            for v in invalid:
                if(v[1] == pos[1] or\
                  abs(pos[0] - v[0]) == abs(pos[1] - v[1])):
                    return False
            return True
        
        count = [0]
        placeQueens(0, list())
        return count[0]