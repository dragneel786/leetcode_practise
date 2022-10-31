class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        ans = prev = 0
        n = len(s)
        
        while(i < n):
            curr = 1
            while(i < n - 1 and s[i] == s[i + 1]):
                i += 1
                curr += 1
            
            ans += min(prev, curr)
            prev = curr
            i += 1
        
        return ans
                