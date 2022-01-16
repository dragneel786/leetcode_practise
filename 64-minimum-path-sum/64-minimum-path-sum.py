class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [grid[0][0]]
        for i in range(1, m):
            dp.append(grid[0][i] + dp[i - 1])

        for i in range(1, n):
            newList = [dp[0] + grid[i][0]]
            for j in range(1, m):
                newList.append(grid[i][j] + min(dp[j], newList[-1]))
            dp = newList

        return dp[-1]