class Solution:
    def findValidPair(self, s: str) -> str:
        counts = Counter(s)
        for i in range(len(s) - 1):
            a, b = int(s[i]), int(s[i + 1])
            if a == b or counts[s[i]] != a or counts[s[i + 1]] != b:
                continue

            return s[i: i + 2]
        
        return ""