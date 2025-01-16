class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        r1 = reduce(lambda a, b: a ^ b, nums1)
        r2 = reduce(lambda a, b: a ^ b, nums2)
        return (r2 if n1 % 2 else 0) ^ (r1 if n2 % 2 else 0)