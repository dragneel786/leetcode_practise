class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [[e for e in s1 if e not in s2],\
                [e for e in s2 if e not in s1]]