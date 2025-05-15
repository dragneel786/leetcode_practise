class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        start = (groups[0] + 1) % 2
        for w, g in zip(words, groups):
            if g != start:
                res.append(w)
                start = g
        
        return res