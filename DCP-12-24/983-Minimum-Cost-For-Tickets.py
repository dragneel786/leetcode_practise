class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def get_ways(idx):
            if idx >= len(days):
                return 0
            
            min_cost = inf
            for i, d in enumerate([0, 6, 29]):
                new_idx = idx
                new_day = days[new_idx] + d
                while(new_idx < len(days) and days[new_idx] <= new_day):
                    new_idx += 1

                min_cost = min(min_cost, costs[i] + get_ways(new_idx))
        
            return min_cost
        
        return get_ways(0)