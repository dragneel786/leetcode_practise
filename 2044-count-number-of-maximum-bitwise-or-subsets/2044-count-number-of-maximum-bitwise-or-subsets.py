class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        
        def sub_or(val, i):
            nonlocal max_set, count
            if(i >= len(nums)):
                if(max_set > val):
                    return 
                
                if(max_set < val):
                    max_set = val
                    count = 0
                    
                count += 1
                return
            
            sub_or(val | nums[i], i + 1)
            sub_or(val, i + 1)
        
        max_set, count = -1, 0
        sub_or(0, 0)
        return count
            
            