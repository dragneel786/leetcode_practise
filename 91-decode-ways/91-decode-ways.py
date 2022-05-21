class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0] == '0'):
            return 0
        
        n = len(s)
        dp = [1] + ([0] * n)
        dp[1] = 1
        for i in range(2, n + 1):
            val1 = int(s[i - 1])
            val2 = int(s[i - 2: i])
            if(val1 != 0):
                dp[i] = dp[i - 1]
            if(10 <= val2 <= 26):
                dp[i] += dp[i - 2]
        
        return dp[n]
                