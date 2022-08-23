class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = ""
        prev = open_para = close_para = 0
        for i, c in enumerate(s):
            
            open_para += c == '('
            close_para += c == ')'
            
            if(open_para == close_para):
                open_para = close_para = 0
                res += s[prev + 1: i]
                prev = i + 1
            
        return res
                
            
                
                
            