class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def min_cost(i = 0):
            if(i >= len(days)):
                return 0
            
            ans = inf
            for c, d in zip(costs, [0, 6, 29]):
                j = i
                while(j < len(days) and days[j] <= days[i] + d):
                    j += 1
                
                ans = min(ans, c + min_cost(j))
            
            return ans
    
        return min_cost()