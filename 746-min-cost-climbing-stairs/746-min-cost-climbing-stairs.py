class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = defaultdict(lambda:math.inf)
        dp[-1] = dp[-2] = 0
        for i in range(n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n - 2])