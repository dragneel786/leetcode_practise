class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def find_res(idx, res = 0):
            if idx >= len(nums):
                return res == target
            
            return find_res(idx + 1, res + nums[idx]) \
        + find_res(idx + 1, res - nums[idx])
        
        return find_res(0)
    
            