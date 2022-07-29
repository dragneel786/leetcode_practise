class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matcher(word):
            p = {}
            return [p.setdefault(w, len(p)) for w in word]
                
        pat = matcher(pattern)
        return filter(lambda w: matcher(w) == pat, words)