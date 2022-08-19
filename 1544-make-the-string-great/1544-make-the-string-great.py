class Solution:
    def makeGood(self, s: str) -> str:
        
        check_validity = lambda a, b: abs(ord(a) - ord(b)) == 32
        
        p = 0
        s = list(s)
        for i in range(len(s)):
            if(p > 0 and check_validity(s[p - 1], s[i])):
                p -= 1
            else:
                s[p] = s[i]
                p += 1
        
        return "".join(s[:p])