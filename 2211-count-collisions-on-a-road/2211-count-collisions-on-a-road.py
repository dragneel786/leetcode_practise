class Solution:
    def countCollisions(self, directions: str) -> int:
        rs = cols = 0
        prev = directions[0]
        col_state = {("R", "S"): 1, ("R", "L"): 2, ("S", "L"): 1}
        
        for curr in directions[1:]:
            print(prev, curr, col_state.get((prev, curr),0))
            if (prev, curr) in col_state:
                cols += col_state[(prev, curr)] + rs
                prev = "S"
                rs = 0

            else:
                if prev == curr == "R":
                    rs += 1
                prev = curr
            
        
        return cols



            

