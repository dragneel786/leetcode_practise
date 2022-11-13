class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w for w in s.split()[::-1] if(len(w) > 0)])