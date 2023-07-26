class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def calculate2(speed):
            return reduce(lambda a, b: ceil(a) + (b / speed), dist)
        
        
        low = 1
        high = 10 ** 9
        dist = [0] + dist
        res = -1
        while(low <= high):
            mid = (high - low) // 2 + low
            if(calculate2(mid) <= hour):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
        
            
            
        