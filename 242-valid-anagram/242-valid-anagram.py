class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        letters = [0] * 26
        for c in s: letters[ord(c) - ord('a')] += 1
        for c in t: letters[ord(c) - ord('a')] -= 1
        return not any(letters)