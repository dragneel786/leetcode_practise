class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def totalCombos(val, memo = {}):
            if(val <= 0):
                return val == 0
            
            if(val in memo): return memo[val]
            
            ret = 0
            for n in nums:
                ret += totalCombos(val - n)
            memo[val] = ret
            return ret
            
        return totalCombos(target)