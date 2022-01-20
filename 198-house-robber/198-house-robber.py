class Solution:
    def rob(self, nums: List[int]) -> int:
        max_wo, max_wi = 0, nums[0]
        for i in range(1, len(nums)):
            val = max_wo + nums[i]
            if(val > max_wi):
                max_wo = max_wi
                max_wi = val
            else:
                max_wo = max_wi

        return max_wi
                