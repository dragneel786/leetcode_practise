class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSub(w):
            i = 0
            for c in w:
                if(not indexes[c]):
                    return False
                idx = bisect_left(indexes[c], i)
                if(idx == len(indexes[c])):
                    return False
                i = indexes[c][idx] + 1
            return True
        
        indexes = defaultdict(lambda:[])
        for i,c in enumerate(s):
            indexes[c].append(i)
        
        res = 0
        for w in words:
            if(isSub(w)):
                res += 1
        
        return res
                
        
        