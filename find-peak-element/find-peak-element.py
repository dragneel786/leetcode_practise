class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, n = 0, len(nums)
        high = n - 1
        if(n == 1):
            return 0

        while(low <= high):
            mid = (low + ((high - low) // 2))
            if((mid == 0 and nums[mid] > nums[mid + 1]) or \
                (mid == n - 1 and nums[mid] > nums[mid - 1])):
                return mid

            if(nums[mid - 1] < nums[mid] > nums[mid + 1]):
                return mid

            if(nums[mid] < nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1