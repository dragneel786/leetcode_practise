class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        if(s[n - 1] != "0"):
            dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if(s[i] == "0"):
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if(int(s[i: i + 2]) < 27):
                    dp[i] += dp[i + 2]

        return dp[0]