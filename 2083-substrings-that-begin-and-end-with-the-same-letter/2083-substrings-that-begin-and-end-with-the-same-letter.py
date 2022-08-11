class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = 0
        seen = Counter()
        for c in s:
            counts += 1 + seen[c]
            seen[c] += 1
        return counts
        