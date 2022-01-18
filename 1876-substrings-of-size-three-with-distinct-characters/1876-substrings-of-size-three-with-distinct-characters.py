class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if(n < 3):
            return 0
        
        # lookup = [0] * 26
        lookup = dict()
        for i in range(3):
            lookup[s[i]] = lookup.get(s[i], 0) + 1
        
        count = 0
        if(self.checkKeys(lookup)):
            count += 1
        
        for i in range(3, n):
            lookup[s[i - 3]] -= 1
            lookup[s[i]] = lookup.get(s[i], 0) + 1
            if(self.checkKeys(lookup)):
                count += 1
        
        return count

    def checkKeys(self, lookup):
        for i in lookup.keys():
            if(lookup[i] > 1):
                return False   
        return True