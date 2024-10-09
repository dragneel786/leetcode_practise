class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = needed = 0
        for c in s:
            if c == ')':
                if opens > 0:
                    opens -= 1
                else:
                    needed += 1
                    
            else:
                opens += 1
        
        return needed + opens
                
            