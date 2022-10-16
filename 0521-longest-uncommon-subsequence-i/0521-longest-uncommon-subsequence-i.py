class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        an, bn = len(a), len(b)
        return max(an, bn) if(a != b) else -1