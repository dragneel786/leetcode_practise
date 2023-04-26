class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []
        n = len(s)
        if(n == 1):
            return s
        
        for i in range(1, n, 2):
            ans.append(s[i - 1])
            ans.append(chr(ord(s[i - 1]) + int(s[i])))
        
        if(i < n - 1):
            ans.append(s[-1])
            
        return ''.join(ans)
            