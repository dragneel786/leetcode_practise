class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @functools.lru_cache(None)
        def minCost(i):
            if(i >= n - 1):
                return cost[i] if(i == n - 1) else 0
            return cost[i] + min(minCost(i + 1), minCost(i + 2))
        
        n = len(cost)
        return min(minCost(0), minCost(1))