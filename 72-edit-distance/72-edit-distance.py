class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[_ + l for _ in range(m + 1)] for l in range(n + 1)]
        # print(dp)
        for i in range(n, 0, -1):
            for j in range(m, 0, -1):
                if(word1[j - 1] == word2[i - 1]):
                    dp[n - i + 1][m - j + 1] = dp[n - i][m - j]
                else:
                    dp[n - i + 1][m - j + 1] = 1 + \
                        min(dp[n - i + 1][m - j], \
                            min(dp[n - i][m - j], dp[n - i][m - j + 1]))

        return dp[n][m]