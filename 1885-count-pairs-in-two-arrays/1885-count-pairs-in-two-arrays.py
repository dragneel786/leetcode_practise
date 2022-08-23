class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums = [x - y for x, y in zip(nums1, nums2)]
        nums.sort()
        
        n = len(nums)
        counts = 0
        for i, x in enumerate(nums):
            idx = bisect_right(nums, -x)
            counts += n - max(i + 1, idx)
        
        return counts
        