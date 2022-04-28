class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)
        
        def operations(mid):
            opr = 0
            for n in nums:
                opr += (n - 1) // mid
            return opr
    
        while(left < right):
            mid = (right - left) // 2 + left
            if(operations(mid) > maxOperations):
                left = mid + 1
            else:
                right = mid
        
        return left
        
        
        
        
        