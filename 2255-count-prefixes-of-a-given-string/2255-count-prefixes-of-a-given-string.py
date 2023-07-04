class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counts = 0
        for word in words:
            m, n = len(word), len(s)
            if(m <= n):
                for a, b in zip(word, s):
                    if(a != b):
                        break
                else:
                    counts += 1
            
        return counts
                