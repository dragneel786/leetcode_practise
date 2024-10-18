class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        
        def counts(idx, val = 0, values = []):
            nonlocal max_val, cc
            if idx >= len(nums):
                if max_val < val:
                    max_val = val
                    cc = 1

                elif max_val == val:
                    cc += 1
                
                return
            
            counts(idx + 1, val | nums[idx], values + [nums[idx]])
            counts(idx + 1, val, values)
        
        max_val = cc = 0
        counts(0)
        return cc
            