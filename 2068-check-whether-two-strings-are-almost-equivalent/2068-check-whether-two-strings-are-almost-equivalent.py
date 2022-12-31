class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counts = [0] * 26
        for c1, c2 in zip(word1, word2):
            counts[ord(c1) - 97] += 1
            counts[ord(c2) - 97] -= 1
            
        return list(filter(lambda x: abs(x) > 3, counts)) == []