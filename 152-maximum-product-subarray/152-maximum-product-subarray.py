class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        res = float("-inf")
        for n in nums:
            val = (n, n * currMax, n * currMin)
            currMax, currMin = max(val), min(val)
            res = max(res, currMax)

        return res