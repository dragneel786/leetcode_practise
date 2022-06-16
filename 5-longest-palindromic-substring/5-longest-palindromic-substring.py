class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [([0] * n) for _ in range(n)]
        res = s[0]
        for i in range(n):
            dp[i][i] = 1
            if(i < n - 1 and s[i] == s[i + 1]):
                dp[i][i + 1] = 1
                res = s[i:i + 2]
        
        for i in range(2, n):
            temp = None
            for j in range(n - i):
                if(s[j] == s[j + i] and dp[j + 1][j + i - 1]):
                    dp[j][j + i] = 1
                    if(not temp):
                        temp = s[j:j + i + 1]
                
            if(temp):
                res = temp
        return res
        
            