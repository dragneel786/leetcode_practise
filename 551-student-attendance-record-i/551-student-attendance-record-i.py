class Solution:
    def checkRecord(self, s: str) -> bool:
        # Go through the string.
        # keep checking the Absent count if it gets >= 2 return False
        # keep checking for the consecutive L if get >= 3 return False
        # return true
        s += "P"
        acount = lcount = 0
        for c in s:
            if(lcount == 3 or acount >= 2):
                return False
            if(c == "L"):
                lcount += 1
                continue
            if(c == "A"):
                acount += 1
            lcount = 0
            
            
        return True
            
            
            
                
        