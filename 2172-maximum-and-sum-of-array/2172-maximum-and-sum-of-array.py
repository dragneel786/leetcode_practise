class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        @lru_cache(None)
        def max_and_sum(index, slots):
            nonlocal numSlots
            if(index == len(nums)):
                return 0

            slots = list(slots)
            max_sum = 0
            for i in range(numSlots):
                if(slots[i] < 2):
                    slots[i] += 1

                    max_sum = max(max_sum, (nums[index] & (i + 1))
                                  + max_and_sum(index + 1, tuple(slots)))

                    slots[i] -= 1

            return max_sum

        slots = tuple([0 for i in range(numSlots)])
        return max_and_sum(0, slots)
        
        
        
                    
            