class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxD = 0
        j = len(nums2) - 1
        for i in range(len(nums1) - 1, -1, -1):
            low = i
            high = j
            found = False
            while(low <= high):
                mid = low + (high - low) // 2
                if(nums2[mid] >= nums1[i]):
                    j = mid
                    found = True
                    low = mid + 1
                else:
                    high = mid - 1
        
            if(found):
                maxD = max(maxD, j - i)
            
        return maxD