class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def isSubSeq(word, counter):
            pos = 0
            for i, c in enumerate(word):
                idx = bisect_left(counter[c], pos)
                if(idx >= len(counter[c])):
                    return False
                pos = counter[c][idx] + 1
            return True
    
        counter = defaultdict(list)
        for i, c in enumerate(s):
            counter[c].append(i)
            
        counts = 0
        for w in words:
            if(isSubSeq(w, counter)):
                counts += 1
        return counts
        
        
        
        