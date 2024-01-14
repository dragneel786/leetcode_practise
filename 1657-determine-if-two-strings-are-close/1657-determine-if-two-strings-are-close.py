class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1) != len(word2)):
            return False
        
        word1_map = Counter(word1)
        word2_map = Counter()
        for c in word2:
            if(c not in word1_map):
                return False
            
            word2_map[c] += 1
            
        values1 = sorted(word1_map.values())
        values2 = sorted(word2_map.values())
        return values1 == values2