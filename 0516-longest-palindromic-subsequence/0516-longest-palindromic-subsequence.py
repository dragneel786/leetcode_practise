class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp_prev = dp.copy()
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, n):
                if(s[i] == s[j]):
                    dp[j] = dp_prev[j - 1] + 2
                else:
                    dp[j] = max(dp_prev[j], dp[j - 1])
            
            dp, dp_prev = dp_prev, dp
        
        return dp_prev[-1]
            