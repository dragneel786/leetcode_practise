class Solution:
    def rob(self, nums: List[int]) -> int:
        max_till = max_so_far = nums[0]
        prev_max = 0
        
        for num in nums[1:]:
            curr_max = max(max_till, prev_max + num)
            max_so_far = max(curr_max, max_so_far)
            if(curr_max == max_till):
                prev_max = max_till
            else:
                prev_max = max_till
                max_till = curr_max
        
        return max_so_far
        