class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = [0] * 26
        for w in words2:
            for k, v in Counter(w).items():
                res[ord(k) - 97] = max(v, res[ord(k) - 97])

        ret = []
        for w in words1:
            counts = Counter(w)
            for i, v in enumerate(res):
                if counts[chr(i + 97)] < v:
                    break
            else:
                ret.append(w)
        
        return ret