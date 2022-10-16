class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        an, bn = len(a), len(b)
        
        if(a != b):
            return max(an, bn)
        
        return -1