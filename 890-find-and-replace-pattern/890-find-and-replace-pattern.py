class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_hash = dict()
        word_hash = dict()
        res = []
        for w in words:
            for c1, c2 in zip(w, pattern):
                val1 = word_hash.get(c1, "")
                val2 = pattern_hash.get(c2, "")
                if((val1 == c2 and val2 == c1) or (val1 == val2 == "")):
                        word_hash[c1] = c2
                        pattern_hash[c2] = c1
                else:
                    break
            else:
                res.append(w)
            word_hash = {}
            pattern_hash = {}
        return res