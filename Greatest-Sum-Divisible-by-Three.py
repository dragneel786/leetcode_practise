class Solution:
    def maxSumDivThree(self, A):
        dp = [0, 0, 0]
        for a in A:
            for i in dp[:]:
                dp[(i + a) % 3] = max(dp[(i + a) % 3], i + a)
        return dp[0]