class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        curr = ""
        n = len(s)
        for c in s[:n//2]:
            curr += c
            m = len(curr)
            if(n % m == 0 and curr * (n // m) == s):
                return True
        
        return False