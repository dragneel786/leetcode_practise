class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces = 0
        s += ' '
        for i, c in enumerate(s):
            spaces += c == ' '
            if(spaces == k):
                break
        
        return s[:i]