class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        ans = set(v if(v in nums1) else -1 for v in nums2)
        if(-1 in ans):
            ans.remove(-1)
        return ans