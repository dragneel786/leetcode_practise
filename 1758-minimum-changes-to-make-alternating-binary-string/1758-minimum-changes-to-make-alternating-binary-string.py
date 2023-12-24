class Solution:
    def minOperations(self, s: str) -> int:
        zchange = ochange = 0
        zp = '0'
        op = '1'
        for i in range(len(s)):
            if(zp != s[i]):
                zchange += 1
            else:
                ochange += 1
            
            zp, op = op, zp
        
        return min(zchange, ochange)
        
            
            
            