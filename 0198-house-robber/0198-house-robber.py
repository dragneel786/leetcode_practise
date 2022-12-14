class Solution:
    def rob(self, nums: List[int]) -> int:
        max_till = 0
        max_so_far = nums[0]
        
        for num in nums[1:]:
            curr_max = max_till + num
            if(curr_max > max_so_far):
                max_till = max_so_far
                max_so_far = curr_max
            else:
                max_till = max_so_far
        
        return max_so_far
        