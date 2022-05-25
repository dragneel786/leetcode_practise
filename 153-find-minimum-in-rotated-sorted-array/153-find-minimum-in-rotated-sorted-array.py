class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while(low <= high):
            mid = (high - low) // 2 + low
            if((mid == 0 or nums[mid - 1] > nums[mid]) and \
              (mid == n - 1 or nums[mid + 1] > nums[mid])):
                return nums[mid]
            
            if(nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid - 1