class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        @lru_cache(None)
        def get_ans(i, start = 0, remain = k):
            if(i >= len(events) or remain <= 0):
                return 0
            
            s, e, v = events[i]
            res = 0
            if(s > start):
                res = get_ans(i + 1, e, remain - 1) + v
            return max(res, get_ans(i + 1, start, remain))
        
        
        events.sort()
        return get_ans(0)