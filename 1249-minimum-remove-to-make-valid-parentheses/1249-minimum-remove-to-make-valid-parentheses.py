class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        closec = s.count(')')
        braces = 0
        res = []
        for c in s:
            if(c not in "()"):
                res.append(c)

            elif(c == '(' and closec > braces):
                res.append(c)
                braces += 1

            elif(c == ')'):
                closec -= 1
                if(braces > 0):
                    res.append(c)
                    braces -= 1

        return ''.join(res)
            
            
                
            
        
        