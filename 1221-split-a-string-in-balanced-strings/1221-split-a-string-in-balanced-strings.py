class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sub = 0
        l = r = 0
        for c in s:
            if(c == 'L'):
                l += 1
            else:
                r += 1
            
            if(l == r):
                sub += 1
                l = r = 0
        
        return sub