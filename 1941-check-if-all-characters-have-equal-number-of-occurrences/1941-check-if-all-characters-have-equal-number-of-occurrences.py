class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        v = Counter(s).values()
        return len(set(v)) == 1