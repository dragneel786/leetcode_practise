class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        
        for i in range(n - 1, -1, -1):
            val = int(s[i])
            if(val == 0): continue
            
            dp[i] = dp[i + 1]
            if(i < n - 1):
                double_val = int(s[i: i + 2])
                if(double_val < 27):
                    dp[i] += dp[i + 2]
            
        return dp[0]
            
        