class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def assignValues(m1, m2):
            l1 = l2 = -math.inf
            r1 = r2 = math.inf
            if(m1 != 0): l1 = nums1[m1 - 1]
            if(m2 != 0): l2 = nums2[m2 - 1] 
            if(m1 != m): r1 = nums1[m1] 
            if(m2 != n): r2 = nums2[m2] 
            return [l1,l2,r1,r2]
        
        med = 0
        m, n = len(nums1), len(nums2)
        if(m > n): return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, m
        while(low <= high):
            cut1 = (low + high) // 2
            cut2 = ((m + n) // 2) - cut1
            l1, l2, r1, r2 = assignValues(cut1, cut2)
            if(l1 > r2): high = cut1 - 1
            elif(r1 < l2): low = cut1 + 1
            else:
                return min(r1, r2) if((m + n) % 2) else (max(l1, l2) + min(r1, r2)) / 2
                
            
                
                