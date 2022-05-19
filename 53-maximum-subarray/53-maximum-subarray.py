class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_till = 0
        max_sofar = -math.inf
        for i in range(len(nums)):
            max_till = max(max_till + nums[i], nums[i])
            max_sofar = max(max_till, max_sofar)
        return max_sofar