class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [([0] * n) for _ in range(n)]
        ans = n
        for i in range(n):
            dp[i][i] = 1
            if(i + 1 < n and s[i] == s[i + 1]):
                dp[i][i + 1] = 1
                ans += 1
            
            
        for size in range(2, n):
            for j in range(n - size):
                if(s[j] == s[j + size] and dp[j + 1][j + size - 1]):
                    dp[j][j + size] = 1
                    ans += 1
                
                
        return ans
            