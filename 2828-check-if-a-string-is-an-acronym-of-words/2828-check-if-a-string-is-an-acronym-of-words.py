class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        idx = 0
        for w in words:
            if(idx >= len(s) or w[0] != s[idx]):
                return False
            
            idx += 1
        
        return idx == len(s)