class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def calc_time(val):
            nonlocal totalTrips
            count = 0
            for t in time:
                count += (val // t)
            return count >= totalTrips
        
        
        ans = totalTrips
        time.sort()
        low = 1
        high = time[-1] * totalTrips
        while(low <= high):
            mid = (low + (high - low) // 2)
            if(calc_time(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans
                
        
        