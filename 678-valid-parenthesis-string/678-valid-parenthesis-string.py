class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open_min = open_max = 0
        for b in s:
            if(b == '('):
                open_min += 1 
                open_max += 1
            
            elif(b == ')'):
                open_min -= 1
                open_max -= 1
            
            else:
                open_min -= 1
                open_max += 1
            
            if(open_max < 0):
                return False
            
            open_min = max(open_min, 0)
        
        return open_min == 0
    
    