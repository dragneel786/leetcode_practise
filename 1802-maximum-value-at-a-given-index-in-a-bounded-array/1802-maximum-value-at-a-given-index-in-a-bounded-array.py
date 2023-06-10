class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low = 1
        high = maxSum
        
        def isValid(mid):
            mid -= 1
            l = index
            r = (n - 1 - index)
            rSum = ((mid * (mid + 1)) // 2)
            lSum = rSum
            if(l <= mid):
                lSum -= ((mid - l) * (mid - l + 1) // 2)
            else:
                lSum += (1 * (l - mid))
            
            if(r <= mid):
                rSum -= ((mid - r) * (mid - r + 1) // 2)
            else:
                rSum += (1 * (r - mid))
        
            return (lSum + rSum + (mid + 1)) <= maxSum
                
            
        res = 0
        while(low <= high):
            mid = (high - low) // 2 + low
            if(isValid(mid)):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res