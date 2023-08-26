class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        counts = Counter(nums2)
        for num in nums1:
            idx = bisect_left(nums2, num)
            if(num in counts):
                return num
        
        return -1
            