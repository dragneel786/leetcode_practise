class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @lru_cache(None)
        def paint_it(idx, remain):
            if(remain <= 0):
                return 0
            
            if(idx == len(cost)):
                return inf
            
            value = min(cost[idx] + paint_it(idx + 1, remain - 1 - time[idx]),\
                        paint_it(idx + 1, remain))
            return value
        
        return paint_it(0, len(cost))