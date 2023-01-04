class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(ws):
            wd = 1
            s = 0
            for w in weights:
                s += w
                if(s > ws):
                    wd += 1
                    s = w
            
            return wd
             
        
        hi = sum(weights)
        lo = max(weights)
        while(lo < hi):
            mid = (hi + lo) // 2
            cd = check(mid)
            if(cd <= days):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
        
        
