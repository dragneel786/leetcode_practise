class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = deque()
        opens = deque()
        for i, c in enumerate(s):
            if(c == '('):
                opens.append((i, c))
            
            elif(c == '*'):
                stars.append((i, c))
            
            else:
                if(len(opens) > 0):
                    opens.pop()
                
                elif(len(stars) > 0):
                    stars.pop()
                
                else: 
                    return False
                
        
        while(len(opens) and len(stars)):
            if(opens[-1][0] > stars[-1][0]):
                return False
            
            opens.pop()
            stars.pop()
        
        
        return len(opens) == 0
                
                
        