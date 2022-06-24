class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_till = 0
        maxsoFar= -math.inf
        for n in nums:
            max_till = max(max_till + n, n)
            maxsoFar = max(maxsoFar, max_till)
        return maxsoFar
            