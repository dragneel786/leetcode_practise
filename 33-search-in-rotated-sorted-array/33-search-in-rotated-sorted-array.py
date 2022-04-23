class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        n = len(nums)
        high = n - 1
        while(low <= high):
            mid = low + (high - low) // 2
            if((mid == 0 or nums[mid] < nums[mid - 1]) and \
               (mid == n - 1 or nums[mid] < nums[mid + 1])):
                val1 = bisect_left(nums, target, 0, mid)
                val2 = bisect_left(nums, target, mid, n)
                print(low, high, val1, val2, mid)
                if(val1 > -1 and val1 < n and nums[val1] == target):
                    return val1
                if(val2 > -1 and val2 < n and nums[val2] == target):
                    return val2
                return -1
            if(nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid - 1
            
            