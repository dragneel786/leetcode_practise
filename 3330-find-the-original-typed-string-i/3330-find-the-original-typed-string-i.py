class Solution:
    def possibleStringCount(self, word: str) -> int:
        counts = idx = 0
        res = 1
        for i, c in enumerate(word + '-'):
            if word[idx] == c:
                counts += 1
            
            else:
                if counts > 1:
                    res += (counts - 1)
                    
                counts = 1
                idx = i 
        
        return res
            