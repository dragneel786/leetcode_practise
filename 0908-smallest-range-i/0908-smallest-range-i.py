class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minv = inf
        maxv = -inf
        for num in nums:
            maxv = max(num, maxv)
            minv = min(num, minv)
        diff = maxv - minv - (k * 2)
        return diff if(diff > 0) else 0
            