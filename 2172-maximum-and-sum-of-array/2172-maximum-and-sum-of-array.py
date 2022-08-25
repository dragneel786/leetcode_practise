class Solution:
    def maximumANDSum(self, nums: List[int], ns: int) -> int:
        
        @lru_cache(None)
        def get_max(index, slots):
            if(index == len(nums)):
                return 0
            
            max_val = 0
            for i in range(1, ns + 1):
                base = 3 ** (i - 1)
                left = (slots // base) % 3
                if(left > 0):
                    max_val = max(max_val, (nums[index] & i) +\
                                  get_max(index + 1, slots - base))
            
            return max_val
        
        return get_max(0, 3 ** ns - 1)
        
        
        
                    
            