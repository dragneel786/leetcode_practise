class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = [0] * 26
        for c in s:
            letters[ord(c) - 97] += 1
        
        for c in t:
            idx = ord(c) - 97
            if(not letters[idx]):
                return c
            else:
                letters[idx] -= 1