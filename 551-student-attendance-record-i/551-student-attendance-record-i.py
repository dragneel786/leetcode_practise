class Solution:
    def checkRecord(self, s: str) -> bool:
        # Go through the string.
        # keep checking the Absent count if it gets >= 2 return False
        # keep checking for the consecutive L if get >= 3 return False
        # return true
        acount = lcount = 0
        for c in s:
            if(c == "L"):
                lcount += 1
            elif(c == "A"):
                acount += 1
                lcount = 0
            else:
                lcount = 0
            
            if(lcount == 3 or acount >= 2):
                return False
        return True
            
            
            
                
        