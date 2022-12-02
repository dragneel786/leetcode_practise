class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m, n = len(word1), len(word2)
        if(m != n):
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        keys1, values1 = c1.keys(), c1.values()
        keys2, values2 = c2.keys(), c2.values()
        
        return sorted(keys1) == sorted(keys2) and\
    sorted(values1) == sorted(values2) 
        
        