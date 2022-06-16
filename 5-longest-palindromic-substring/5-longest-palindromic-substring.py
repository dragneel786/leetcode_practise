class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [([0] * n) for _ in range(n)]
        lo, hi = 0, 1
        for i in range(n):
            dp[i][i] = 1
            if(i < n - 1 and s[i] == s[i + 1]):
                dp[i][i + 1] = 1
                lo = i
                hi = i + 2
        
        
        for i in range(2, n):
            for j in range(n - i):
                if(s[j] == s[j + i] and dp[j + 1][j + i - 1]):
                    dp[j][j + i] = 1
                    lo, hi = j, j + i + 1
        
        return s[lo: hi]
        
            