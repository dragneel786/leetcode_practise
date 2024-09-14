class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = val = nums[0]
        start = 0
        max_size = 1
        for i in range(1, len(nums)):
            if nums[i] <= (val & nums[i]) >= val:
                val &= nums[i]
            else:
                val = nums[i]
                start = i

            if max_val <= val:
                if max_val < val:
                    max_size = i - start + 1
                else:
                    max_size = max(max_size, i - start + 1)
                max_val = val

        return max_size