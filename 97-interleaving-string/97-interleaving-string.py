class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if(m + n != len(s3)):
            return False

        dp = [([False] * (m + 1)) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if(i == 0 and j == 0):
                    dp[i][j] = True
                elif(i == 0):
                    dp[i][j] = dp[i][j - 1] if(s1[j - 1] == s3[i + j - 1]) else False
                elif(j == 0):
                    dp[i][j] = dp[i - 1][j] if(s2[i - 1] == s3[i + j - 1]) else False
                else:
                    if(s2[i - 1] == s3[i + j - 1]):
                        dp[i][j] = dp[i - 1][j]

                    if(not dp[i][j] and s1[j - 1] == s3[i + j - 1]):
                        dp[i][j] = dp[i][j - 1]

        return dp[n][m]