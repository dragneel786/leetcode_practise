class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            temp = [0] * n
            temp[-1] = dp[-1]
            
            for j in range(n - 2, -1, -1):
                temp[j] = temp[j + 1] + dp[j]
            
            dp = temp
        
        return dp[0]