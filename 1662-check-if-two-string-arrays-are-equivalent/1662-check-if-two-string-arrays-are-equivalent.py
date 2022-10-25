class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        m, n = len(word1), len(word2)
        if(m < n):
            return self.arrayStringsAreEqual(word2, word1)
        
        idx = i = 0
        for w in word1:
            for c in w:
                if(idx == n or \
                   c != word2[idx][i]):
                    return False
                
                i += 1
                if(i == len(word2[idx])):
                    idx += 1
                    i = 0
                    
        return idx == n