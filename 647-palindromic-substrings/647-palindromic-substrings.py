class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [([False] * n) for _ in range(n)]
        counts = 0
        for i in range(n):
            dp[i][i] = True
            counts += 1
            if(i < n - 1 and s[i] == s[i + 1]):
                dp[i][i + 1] = True
                counts += 1
        
        for i in range(2, n):
            for j in range(n - i):
                if(s[j] == s[j + i] and dp[j + 1][j + i - 1]):
                    dp[j][j + i] = True
                    counts += 1
        
        return counts