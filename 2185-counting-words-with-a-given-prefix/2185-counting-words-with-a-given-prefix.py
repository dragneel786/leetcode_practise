class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(len(w) >= len(pref) and pref == w[:len(pref)] for w in words)