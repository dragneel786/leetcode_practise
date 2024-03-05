class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n - 1
        while(i < j and s[i] == s[j]):
            while(i + 1 < j and s[i + 1] == s[j]):
                i += 1
            
            while(j - 1 > i and s[j - 1] == s[i]):
                j -= 1
            
            i += 1
            j -= 1
            
        
        return j - i + 1
            