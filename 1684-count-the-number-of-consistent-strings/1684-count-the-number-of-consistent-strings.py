class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s1 = set(allowed)
        return sum([set(w).issubset(s1) for w in words])
        