class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        n = len(nums)
        high = n - 1
        while(low <= high):
            mid = (high - low) // 2 + low
            if((mid == 0 or nums[mid - 1] < nums[mid]) and \
               (mid == n - 1 or nums[mid] > nums[mid + 1])):
                return mid
            
            if(mid != 0 and nums[mid - 1] > nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
            