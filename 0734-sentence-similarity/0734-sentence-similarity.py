class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        m, n = len(sentence1), len(sentence2)
        res = False
        if(m == n):
            pairs = defaultdict(set)
            for a, b in similarPairs:
                pairs[a].add(b)
                pairs[b].add(a)
                
            for a, b in zip(sentence1, sentence2):
                if(a != b and a not in pairs[b]):
                    break
            else:
                res = True
            
        return res