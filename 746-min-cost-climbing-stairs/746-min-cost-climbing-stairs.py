class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [cost[0], cost[1]]
        for i in range(2, n):
            dp[0], dp[1] = dp[1], min(dp[0] + cost[i], dp[1] + cost[i])
        return min(dp)
        
#     def getMinCost(self, cost):
#         n = len(cost)
#         if(n == 1):
#             return cost[0]
#         if(n <= 2):
#             dp = [cost[0], cost[0] + cost[1]]
#         else:
#             dp = [cost[0] + cost[1], cost[0] + cost[2]]
#         for i in range(3, n):
#             dp[0], dp[1] = dp[1], min(cost[i] + dp[0], cost[i] + dp[1])

#         return min(dp)