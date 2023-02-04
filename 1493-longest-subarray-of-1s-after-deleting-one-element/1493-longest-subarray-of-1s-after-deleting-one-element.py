class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def get_size(i = 0, c = 0, remain = 1):
            if(i == len(nums)):
                return c - remain
            
            if(not nums[i] and not remain):
                return c
                
            ret = -inf
            if(nums[i] == 0):
                ret = get_size(i + 1, 0, remain)
            return max(ret, get_size(i + 1, c + (nums[i] == 1),\
                                     remain - (nums[i] == 0)))
            
        return get_size()
            
            