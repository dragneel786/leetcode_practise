class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        return sum([c1[k] == c2[k] == 1 for k in c1 & c2])