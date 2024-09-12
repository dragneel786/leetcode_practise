class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_set = set(list(allowed))
        res = 0
        for word in words:
            if len(set(list(word)) - allow_set) == 0:
                   res += 1
        
        return res