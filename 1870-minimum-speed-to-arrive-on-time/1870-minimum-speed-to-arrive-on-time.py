class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if(n - 1 >= hour):
            return -1
        low = 1
        high = 10 ** 9
        
        def isValid(m):
            h = 0
            for i in range(len(dist) - 1):
                h += math.ceil(dist[i] / m)
            h += (dist[-1] / m)
            return h <= hour
                
        
        res = -1
        while(low <= high):
            m = (high - low) // 2 + low
            if(isValid(m)):
                high = m - 1
                res = m
            else:
                low = m + 1
        return res