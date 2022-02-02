class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        large = 0
        for i in range(1, rows + 1):
            ans = [0] * (cols + 1)
            for j in range(1, cols + 1):
                if(int(matrix[i - 1][j - 1])):
                    ans[j] = 1 + min(dp[j - 1], dp[j], ans[j - 1])
                    large = max(ans[j], large)
            dp = ans

        return large * large