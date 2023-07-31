class Solution:
    @lru_cache(None)
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if(not s1 and not s2):
            return 0
        
        if(not s1):
            return sum([ord(c) for c in s2])
        
        if(not s2):
            return sum([ord(c) for c in s1])
        
        if(s1[0] == s2[0]):
            return self.minimumDeleteSum(s1[1:], s2[1:])
        
        return min(ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2),\
                   ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:]))
        
        
        