class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matcher(word):
            p = {}
            for w, x in zip(word, pattern):
                if(p.setdefault(w, x) != x):
                    return False
            return len(set(p.values())) == len(p.values())
        
        return filter(matcher, words)