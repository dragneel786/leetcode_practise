class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calcy(speed):
            nonlocal h
            res = 0
            for p in piles:
                res += (p // speed)
                res += (p % speed != 0)
            
            return res <= h
        
        
        ans = low = 1
        high = max(piles) + 1
        while(low <= high):
            mid = (low + (high - low) // 2)
            if(calcy(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans