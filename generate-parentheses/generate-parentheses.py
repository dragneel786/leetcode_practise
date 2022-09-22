class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def para_combos(o, c, op = ""):
            if(o == 0 and c == 0):
                res.append(op)
                return
            
            if(o > 0):
                para_combos(o - 1, c, op + '(')
                
            if(c > 0 and c > o):
                para_combos(o, c - 1, op + ')')
            
            
        
        res = []
        para_combos(n, n)
        return res