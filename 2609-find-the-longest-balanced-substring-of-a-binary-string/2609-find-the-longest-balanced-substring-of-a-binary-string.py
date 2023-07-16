class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        first_zero = s.find('0')
        if(first_zero == -1):
            return 0
        
        s += '0'
        fone = False
        max_count = 0
        zcount = ocount = 0
        for i, c in enumerate(s[first_zero:], first_zero):
            if(c == '0'):
                if(fone):
                    max_count = max(min(zcount, ocount) * 2, max_count)
                    fone = False
                    zcount = ocount = 0
                
                zcount += 1
                
            elif(c == '1'):
                fone = True
                ocount += 1
            
        return max_count
            
            
            