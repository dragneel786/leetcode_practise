class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        def minCost(i, memo = {}):
            if(i >= n - 1):
                return cost[i] if(i == n - 1) else 0
            
            if(i not in memo):
                memo[i] = cost[i] + min(minCost(i + 1), minCost(i + 2))
            return memo[i]
        
        n = len(cost)
        return min(minCost(0), minCost(1))