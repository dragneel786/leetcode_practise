class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        m, n = len(sentence1), len(sentence2)
        res = False
        if(m == n):
            pairs = set([a + '-' + b for a, b in similarPairs])
            for a, b in zip(sentence1, sentence2):
                if(a != b and a+'-'+b not in pairs\
                   and b + '-' + a not in pairs):
                    break
            else:
                res = True
            
        return res