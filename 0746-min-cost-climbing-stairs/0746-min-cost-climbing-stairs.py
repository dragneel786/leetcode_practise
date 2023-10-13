class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[:2] = cost[:2]
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1], dp[i - 2])
            if(i < n):
                dp[i] += cost[i]
        
        return dp[-1]
        
        
            
            
        
        