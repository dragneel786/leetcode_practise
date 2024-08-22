class Solution:
    def reverseWords(self, s: str) -> str:
        splits = s.split(" ")
        ret = []
        for w in splits:
            if len(w) > 0:
                ret.append(w)
        
        return " ".join(ret[::-1])