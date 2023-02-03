class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        m, n = len(sentence1), len(sentence2)
        res = False
        if(m == n):
            pair_fun = lambda a, b: (a, b) if(a < b) else (b, a)
            pairs = set([pair_fun(a, b) for a, b in similarPairs])
            
            for a, b in zip(sentence1, sentence2):
                if(a != b and pair_fun(a, b) not in pairs):
                    break
            else:
                res = True
            
        return res