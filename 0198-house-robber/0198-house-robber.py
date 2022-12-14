class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def rob_it(idx):
            if(idx >= len(nums)):
                return 0
            
            return max(rob_it(idx + 2) + nums[idx], rob_it(idx + 1))
            
        return max(rob_it(0), rob_it(1))