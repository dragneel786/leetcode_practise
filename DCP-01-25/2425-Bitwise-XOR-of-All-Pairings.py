class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        r1 = r2 = 0
        if len(nums1) % 2: r2 = reduce(lambda a, b: a ^ b, nums2)
        if len(nums2) % 2: r1 = reduce(lambda a, b: a ^ b, nums1)
        return r1 ^ r2