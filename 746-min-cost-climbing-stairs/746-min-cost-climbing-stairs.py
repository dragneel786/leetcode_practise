class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.getMinCost(cost), self.getMinCost(cost[1:]))
        
    def getMinCost(self, cost):
        n = len(cost)
        if(n == 1):
            return cost[0]
        if(n <= 2):
            dp = [cost[0], cost[0] + cost[1]]
        else:
            dp = [cost[0] + cost[1], cost[0] + cost[2]]
        for i in range(3, n):
            dp[0], dp[1] = dp[1], min(cost[i] + dp[0], cost[i] + dp[1])

        return min(dp)