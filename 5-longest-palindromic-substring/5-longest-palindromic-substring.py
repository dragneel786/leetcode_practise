class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def findLP(s, j, k):
            while(j > -1 and k < n and s[j] == s[k]):
                j -= 1
                k += 1
            return s[j + 1:k]
        
        res = s[0]
        for i in range(n):
            res = max(findLP(s, i, i), findLP(s, i, i + 1), res, key=len)
        return res
        
                
        
            