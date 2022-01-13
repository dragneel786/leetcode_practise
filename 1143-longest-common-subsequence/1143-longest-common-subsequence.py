class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = [[float("-inf") for _ in range(m + 1)] for _ in range(n + 1)]
        return self.getLcs(text1, text2, n - 1, m - 1, memo)

    def getLcs(self, text1, text2, i, j, memo):    
        if(i < 0 or j < 0):
            memo[i][j] = 0
            return 0

        if(memo[i][j] != float('-inf')):
            return memo[i][j]

        if(text1[i] == text2[j]):
            memo[i][j] = 1 + self.getLcs(text1, text2, i - 1, j - 1, memo)
        else:
            memo[i][j] = max(self.getLcs(text1, text2, i - 1, j, memo),\
             self.getLcs(text1, text2, i, j - 1, memo))

        return memo[i][j]