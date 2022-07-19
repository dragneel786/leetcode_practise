class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        while(low <= high):
            mid = ((high - low) >> 1) + low
            if((mid == 0 or nums[mid] > nums[mid - 1]) and\
              (mid == n - 1 or nums[mid] > nums[mid + 1])):
                return mid
            
            if(mid != 0 and nums[mid] < nums[mid - 1]):
                high = mid - 1
            else:
                low = mid + 1
        
            