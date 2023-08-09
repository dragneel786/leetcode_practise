class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def check(m, k):
            i = 0
            while(i < len(nums) - 1):
                if((nums[i + 1] - nums[i]) <= m):
                    i += 2
                    k -= 1
                else:
                    i += 1
                
                if(not k):
                    return True
            
            return False
        
        nums.sort()
        low = 0
        res = high = 10 ** 9
        while(low <= high):
            mid = low + ((high - low) // 2)
            if(check(mid, p)):
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        
        return res if(p) else 0