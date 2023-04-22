class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for j in range(1, n + 1):
            dp[0][j] = inf
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if(s1[i - 1] == s2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j] + 1
         
        min_len = inf
        pos = -1
        for i in range(1, m + 1):
            
            if(dp[i][n] < min_len):
                min_len = dp[i][n]
                pos = i - 1
        
        if(min_len == inf):
            return ""
        
        return s1[pos - min_len + 1: pos + 1]
        
        
                    