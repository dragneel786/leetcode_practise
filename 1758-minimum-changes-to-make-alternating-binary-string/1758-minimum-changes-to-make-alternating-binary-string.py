class Solution:
    def minOperations(self, s: str) -> int:
        zchange = ochange = 0
        zp = '0'
        op = '1'
        for i in range(len(s)):
            zchange += zp != s[i]
            ochange += op != s[i]
            zp, op = op, zp
        
        return min(zchange, ochange)
        
                