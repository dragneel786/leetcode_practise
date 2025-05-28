class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr_inc = curr_dec = 0
        max_inc = max_dec = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                curr_dec = curr_inc = 0
                continue

            curr_inc += -curr_inc if(nums[i] > nums[i + 1]) else 1
            curr_dec += -curr_dec if(nums[i] < nums[i + 1]) else 1
            
            max_inc = max(max_inc, curr_inc)
            max_dec = max(max_dec, curr_dec)
        
        return max(max_inc, max_dec) + 1
                