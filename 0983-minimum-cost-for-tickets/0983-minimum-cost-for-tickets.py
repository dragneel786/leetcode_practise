class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def min_cost(i, curr):
            if(i >= len(days)):
                return 0
            
            if(curr >= days[i]):
                return min_cost(i + 1, curr)
            
            ans = inf
            for c, d in zip(costs, [0, 6, 29]):
                ans = min(ans, c + \
                          min_cost(i + 1, days[i] + d))
            
            return ans
        
        return min_cost(0, days[0] - 1)