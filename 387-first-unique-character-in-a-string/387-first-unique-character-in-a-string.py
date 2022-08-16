class Solution:
    def firstUniqChar(self, s: str) -> int:
        C = Counter(s)
        for i, k in enumerate(s):
            if(C[k] == 1):
                return i
        
        return -1