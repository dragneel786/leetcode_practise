class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if(not s):
            return 1
        
        if(s[0] == '0'):
            return 0
        
        ret = self.numDecodings(s[1:])  
        if(len(s) >= 2 and int(s[:2]) <= 26):
            ret += self.numDecodings(s[2:])
        
        return ret