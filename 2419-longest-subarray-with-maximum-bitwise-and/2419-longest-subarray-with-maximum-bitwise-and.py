class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = nums[0]
        max_curr = nums[0]
        curr_size = max_size = 1
        for i in range(1, len(nums)):
            if nums[i] > (max_curr & nums[i]) or \
                (max_curr & nums[i]) < max_curr:
                curr_size = 0
            max_curr = max(max_curr & nums[i], nums[i])
            curr_size += 1
            if max_curr >= max_val:
                if max_curr == max_val:
                    max_size = max(curr_size, max_size)
                else:
                    max_size = curr_size

                max_val = max_curr

        return max_size