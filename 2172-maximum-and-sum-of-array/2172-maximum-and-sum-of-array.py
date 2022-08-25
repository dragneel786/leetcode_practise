class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        def validate(slots, pos):
            pos *= 2
            d1, d2 = (1 << (pos - 2)), (1 << (pos - 1))
            if(slots & d1): return d1
            if(slots & d2): return d2
            return -1
        
        @lru_cache(None)
        def max_and_sum(index, slots):
            nonlocal numSlots
            if(index == len(nums)):
                return 0

            max_sum = 0
            for i in range(1, numSlots + 1):
                value = validate(slots, i)
                if(value == -1): continue
                    
                asum = nums[index] & i
                max_sum = max(max_sum, asum +
                              max_and_sum(index + 1,
                                          slots ^ value))
                
            return max_sum

        slots = (1 << (numSlots * 2)) - 1
        return max_and_sum(0, slots)
        
        
        
                    
            