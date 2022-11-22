class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        pairs = {tuple(sp) for sp in similarPairs}
        for a, b in zip_longest(sentence1, sentence2):
            if(a != b and (a, b) not in pairs\
               and (b, a) not in pairs):
                return False
        
        return True