class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        dp = [0] * cols
        for r in range(rows):
            for c in range(cols):
                dp[c] += points[r][c]
            
            for c in range(1, cols):
                dp[c] = max(dp[c], dp[c - 1] - 1)
            
            for c in range(cols - 2, -1, -1):
                dp[c] = max(dp[c], dp[c + 1] - 1)
            
        return max(dp)
                