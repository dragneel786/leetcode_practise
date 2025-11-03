class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        start, end = min(nums), max(nums)
        nums = set(nums)
        for v in range(start, end + 1):
            if v not in nums:
                res.append(v)
        
        return res
