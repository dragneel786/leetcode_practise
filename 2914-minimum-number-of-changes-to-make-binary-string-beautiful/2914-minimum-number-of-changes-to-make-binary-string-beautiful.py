class Solution:
    def minChanges(self, s: str) -> int:
        counts = 1
        change = 0
        n = len(s)
        i = 1
        while(i < n):
            if s[i] != s[i - 1]:
                if counts & 1:
                    change += 1
                    i += 1
                    counts = 0
            
            i += 1
            counts += 1
        
        return change
                
                