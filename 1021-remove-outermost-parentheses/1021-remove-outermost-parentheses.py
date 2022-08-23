class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        add_sub = lambda c: 1 if(c == ')') else -1
        
        res = ""
        prev = paras = 0
        for i, c in enumerate(s):
            paras += add_sub(c)
            
            if(not paras):
                res += s[prev + 1: i]
                prev = i + 1
            
        return res
                
            
                
                
            