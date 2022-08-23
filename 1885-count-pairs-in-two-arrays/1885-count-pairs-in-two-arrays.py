class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        
        def create_pairs():
            nonlocal nums1, nums2
            for i in range(len(nums1)):
                nums1[i], nums2[i] = (nums1[i] - nums2[i]),\
                (nums2[i] - nums1[i])
        
        
        create_pairs()
        sorted_values = [nums1[0]]
        
        counts = 0
        for j in range(1, len(nums2)):
            idx = bisect_right(sorted_values, nums2[j])
            counts += (len(sorted_values) - idx)
            insort(sorted_values, nums1[j])
        
        return counts
        