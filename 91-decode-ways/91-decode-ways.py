class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0] == "0"):
            return 0
        n = len(s)
        dp = [0] * n
        if(s[n - 1] != "0"):
            dp[-1] = 1
        for i in range(n - 2, -1, -1):
            if(s[i] != '0'):
                dp[i] = dp[i + 1]
                if(int(s[i: i + 2]) <= 26):
                    if(i + 2 < n):
                        dp[i] += dp[i + 2]
                    else:
                        dp[i] += 1

        return dp[0]