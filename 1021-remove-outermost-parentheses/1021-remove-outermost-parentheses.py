class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = []
        temp = []
        open_para = close_para = 0
        for c in s:
            temp.append(c)
            
            open_para += c == '('
            close_para += c == ')'
            
            if(open_para == close_para):
                open_para = close_para = 0
                res.append(''.join(temp[1:-1]))
                temp.clear()
            
        return ''.join(res)
                
            
                
                
            