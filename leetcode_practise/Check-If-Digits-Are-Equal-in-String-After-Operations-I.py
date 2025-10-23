class Solution:
    def hasSameDigits(self, s: str) -> bool:
        sn = len(s)
        while(sn > 2):
            res = []
            for i in range(sn - 1):
                res.append((int(s[i]) + int(s[i + 1])) % 10)
            
            s = ''.join(list(map(str, res)))
            sn = len(s)
        
        return s[0] == s[1]
