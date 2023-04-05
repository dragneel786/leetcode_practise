class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def mid_fine(mid):
            n = len(nums) - 1
            carry = 0
            for i in range(n, 0, -1):
                tot = nums[i] + carry
                if(tot > mid):
                    carry = tot - mid
                else:
                    carry = 0
            
            return nums[0] + carry <= mid
        
        
        
        low = 1
        high = max(nums)
        ans = 0
        while(low <= high):
            mid = low + (high - low) // 2
            if(mid_fine(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans