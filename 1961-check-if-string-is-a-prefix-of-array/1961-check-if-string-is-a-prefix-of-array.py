class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        si = 0
        sn = len(s)
        for word in words:
            wn = len(word)
            if(sn - si < wn or s[si : si + wn] != word):
                return False
            
            si = (si + wn)
            if(si >= sn):
                break
        
        return si >= sn
            
            