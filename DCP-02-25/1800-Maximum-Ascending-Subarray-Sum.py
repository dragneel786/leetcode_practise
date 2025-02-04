class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = curr_sum = val = 0
        for num in nums:
            if val >= num:
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0

            val = num
            curr_sum += num
        
        return max(curr_sum, max_sum)