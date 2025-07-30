class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_so_far = max_curr = nums[0]
        max_len = curr_len = 1
        for num in nums[1:]:
            if max_curr & num < num:
                max_curr = num
                curr_len = 1
            else:
                max_curr &= num
                curr_len += 1
            
            if max_so_far <= max_curr:
                if max_so_far < max_curr:
                    max_len = curr_len
                else:
                    max_len = max(max_len, curr_len)
                
                max_so_far = max_curr
        
        return max_len