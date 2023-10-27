class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [([0] * n) for _ in range(n)]
        start = end = 0
        for i in range(n):
            dp[i][i] = 1
            if(i < n - 1 and s[i] == s[i + 1]):
                dp[i][i + 1] = 1
                start = i
                end = i + 1
        
        for size in range(2, n):
            for i in range(n - size):
                if(s[i] == s[i + size]):
                    dp[i][i + size] = dp[i + 1][i + size - 1]

                if(dp[i][i + size]):
                    start, end = i, i + size
                    
        return s[start: end + 1]