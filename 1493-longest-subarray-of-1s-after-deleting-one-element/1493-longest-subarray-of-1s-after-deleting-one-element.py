class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def get_size(i = 0, c = 0, remain = 1):
            if(i == len(nums)):
                return c - remain
            
            if(not nums[i]):
                if(not remain):
                    return c
                
                return max(get_size(i + 1, c, remain - 1),\
                           get_size(i + 1, 0, remain))
            else:
                return get_size(i + 1, c + 1, remain)
            
            
        
        return get_size()
            
            