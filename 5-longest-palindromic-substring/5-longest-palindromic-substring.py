class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [([0] * n) for _ in range(n)]
        res = s[0]
        for i in range(n):
            dp[i][i] = 1

        length = 1
        for i in range(1, n):
            for j in range(0, n - i):
                if(s[j] == s[j + i] and (i == 1 or dp[j + 1][j + i - 1])):
                    # if(i + 1 > length):
                    res = s[j : j + i + 1]
                        # length = i + 1
                    dp[j][j + i] = 1

        return res