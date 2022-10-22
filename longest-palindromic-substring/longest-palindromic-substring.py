class Solution:
    def longestPalindrome(self, s: str) -> str:
        def intialize():
            nonlocal ans
            dp = [([0] * n) for _ in range(n)]
            for i in range(n):
                dp[i][i] = 1
                if(i < n - 1 and s[i] == s[i + 1]):
                    dp[i][i + 1] = 2
                    ans = (i, i + 1)
            
            return dp
            
        n = len(s)
        ans = (0, 0)
        dp = intialize()
        
        for i in range(2, n):
            for j in range(i, n):
                if(s[j - i] == s[j] and\
                   dp[j - i + 1][j - 1]):
                    ans = (j - i, j)
                    dp[j - i][j] = ans[1] - ans[0]
        
        return s[ans[0]: ans[1] + 1]
                
        
        
        
        
        