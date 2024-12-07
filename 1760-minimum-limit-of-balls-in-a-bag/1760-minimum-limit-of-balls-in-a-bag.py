class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def check(mid):
            ops = 0
            for num in nums:
                if num > mid:
                    ops += (num // mid + (num % mid != 0)) - 1
            
            return ops <= maxOperations
                 
            
        low = 1
        res = high = max(nums)
        while(low <= high):
            mid = low + ((high - low) // 2)
            if check(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
            
            
         