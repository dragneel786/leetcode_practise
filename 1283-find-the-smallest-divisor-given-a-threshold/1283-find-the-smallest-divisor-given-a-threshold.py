class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        
        def divisor(mid):
            res = 0
            for n in nums:
                res += math.ceil(n / mid)
            return res
        
        ans = float('inf')
        while(low <= high):
            mid = (high - low) // 2 + low
            if(divisor(mid) <= threshold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans