class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        high = n - 1
        low = 0
        while(low <= high):
            mid = (low + ((high - low) // 2))
            if(nums[mid] == target):
                return mid

            if(nums[mid] <  target <= nums[high] or \
                target > nums[mid] >= nums[low]  or \
                nums[mid] >= nums[low] > target):
                low = mid + 1

            else: 
                high = mid - 1

        return -1