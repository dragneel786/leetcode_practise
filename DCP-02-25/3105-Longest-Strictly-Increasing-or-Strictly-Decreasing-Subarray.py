class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr_inc = curr_dec = 0
        max_inc = max_dec = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_inc += 1
                curr_dec = 0
            
            elif nums[i] > nums[i + 1]:
                curr_dec += 1
                curr_inc = 0
            
            else:
                curr_dec = curr_inc = 0
            
            max_inc = max(max_inc, curr_inc)
            max_dec = max(max_dec, curr_dec)
        
        return max(max_inc, max_dec) + 1
                