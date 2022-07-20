class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = defaultdict(list)
        for w in words:
            heads[w[0]].append(iter(w[1:]))
        
        for c in s:
            for it in heads.pop(c, []):
                heads[next(it, None)].append(it)
        return len(heads[None])
                
                
        
        
        
        