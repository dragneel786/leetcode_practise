class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def get_max(i, is_even = True):
            if i >= len(nums):
                return 0
            
            val = get_max(i + 1, is_even)
            if is_even:
                return max(val, get_max(i + 1, not is_even) + nums[i])
            
            else:
                return max(val, get_max(i + 1, not is_even) - nums[i])
            
            
        return get_max(0)