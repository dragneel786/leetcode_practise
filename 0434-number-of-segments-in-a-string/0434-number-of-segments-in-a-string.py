class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        found = False
        for c in s:
            if(c != ' '):
                found = True
            else:
                ans += found
                found = False
        
        return ans + found