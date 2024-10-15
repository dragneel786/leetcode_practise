class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        s = list(s)
        start = tot = 0
        end = n - 1
        while(start < end):
            while(start < n and s[start] != '1'):
                start += 1
            
            while(end > -1 and s[end] != '0'):
                end -= 1
            
            if start >= end:
                break
                
            s[start], s[end] = s[end], [start]
            tot += (end - start)
        
        return tot
            
        
            
        