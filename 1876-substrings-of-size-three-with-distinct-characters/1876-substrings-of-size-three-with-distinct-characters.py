class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if(n < 3):
            return 0
        
        lookup = [0] * 26
        for i in range(3):
            lookup[ord(s[i]) - 97] += 1
        
        count = 0
        if(self.containsOnes(lookup)):
            count += 1
        
        for i in range(3, n):
            lookup[ord(s[i - 3]) - 97] -= 1
            lookup[ord(s[i]) - 97] += 1
            if(self.containsOnes(lookup)):
                count += 1
        
        return count
    
    def containsOnes(self, lookup):
        for i in lookup:
            if(i > 1):
                return False
        
        return True