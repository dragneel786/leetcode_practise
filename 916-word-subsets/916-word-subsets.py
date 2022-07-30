class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def checkUniversal(w, combine):
            W = Counter(w)
            return all(W[k] >= v for k,v in combine.items())
        
        combine = Counter()
        for w in words2:
            for k, v in Counter(w).items():
                combine[k] = max(combine[k], v)
            
        return filter(lambda w:checkUniversal(w, combine), words1)