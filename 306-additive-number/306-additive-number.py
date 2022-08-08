class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def isAdditive(val, prev = 0, curr = 0, breaks = 0):
            if(not val): return breaks > 2
            
            temp_val = 0
            for i, v in enumerate(val):
                temp_val = (temp_val * 10) + int(v)
                
                if(i > 0 and val[0] == '0'):
                    return False
                
                elif(breaks > 1 and temp_val == curr + prev\
                   and isAdditive(val[i + 1:],\
                   curr, temp_val, breaks + 1)):
                    return True
                
                elif(breaks < 2 and isAdditive(val[i + 1:],\
                         curr, temp_val, breaks + 1)):
                    return True
            
            return False
        
        return isAdditive(num)
                    