class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def is_prefix_n_suffix(a, b):
            if(len(a) > len(b)):
                return False
            minl = len(a)
            return a[:minl] == b[:minl] and a[-minl:] == b[-minl:]
        
        
        res = 0
        for i, a in enumerate(words):
            for b in words[i + 1:]:
                res += is_prefix_n_suffix(a, b)
        
        return res