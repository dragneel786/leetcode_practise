class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        len2 = len(nums2)
        for num in nums1:
            idx = bisect_left(nums2, num)
            if(idx < len2 and nums2[idx] == num):
                return num
        
        return -1
            