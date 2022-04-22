class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maxD = 0
        for i in range(len(nums1)):
            low = i
            high = len(nums2) - 1
            j = -1
            while(low <= high):
                mid = low + (high - low) // 2
                if(nums2[mid] >= nums1[i]):
                    j = mid
                    low = mid + 1
                else:
                    high = mid - 1
        
            if(j != -1):
                maxD = max(maxD, j - i)
            
        return maxD