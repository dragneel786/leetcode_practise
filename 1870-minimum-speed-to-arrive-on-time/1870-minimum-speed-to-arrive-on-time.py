class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def calculate(speed):
            time_taken = 0
            for d in dist:
                time_taken = ceil(time_taken) + (d / speed)
            return time_taken
        
        
        low = 1
        high = 10 ** 9
        res = -1
        while(low <= high):
            mid = (high - low) // 2 + low
            if(calculate(mid) <= hour):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
        
            
            
        