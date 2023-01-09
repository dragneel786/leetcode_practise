class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        mn = inf
        for num in nums:
            mn = min(num, mn)
            res = max(res, num - mn)
        
        return -1 if(res == 0) else res