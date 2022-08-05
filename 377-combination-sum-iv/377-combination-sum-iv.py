class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def totalCombos(val):
            if(val <= 0):
                return val == 0
            
            ret = 0
            for n in nums:
                ret += totalCombos(val - n)
            return ret
            
        return totalCombos(target)