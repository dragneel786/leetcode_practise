class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def checkUniversal(w, combine):
            W = Counter(w)
            return all(W[k] >= v for k,v in combine.items())
        
        
        combine = Counter()
        for w in words2:
            temp_counter = Counter(w)
            for k in temp_counter:
                combine[k] = max(combine[k], temp_counter[k])
            
        return filter(lambda w:checkUniversal(w, combine), words1)