class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        rows = len(text1)
        cols = len(text2)
        dp = [([0] * (cols + 1)) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                val = max(dp[r][c + 1], dp[r + 1][c])
                if text1[r] == text2[c]:
                    val = max(dp[r][c] + 1, val)
                
                dp[r + 1][c + 1] = val
        
        
        return dp[rows][cols]
                    