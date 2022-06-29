class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def compute():
            ret = 0
            for t in time:
                ret += (mid // t)
            return ret
        
        low, high = 1, min(time) * totalTrips
        res = 0
        while(low <= high):
            mid = (high - low) // 2 + low
            tt = compute()
            if(tt >= totalTrips):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
                