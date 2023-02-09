class Solution:
    def checkString(self, s: str) -> bool:
        switch = False
        for c in s:
            if(c == 'a' and switch):
                return False
            
            if(c == 'b'):
                switch = True
        
        return True