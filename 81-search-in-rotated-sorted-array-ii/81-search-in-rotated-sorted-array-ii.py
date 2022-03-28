class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        h = n - 1
        l = 0
        while(l <= h):
            mid = l + (h - l) // 2
            if(nums[mid] == target):
                return True

            if(nums[mid] == nums[l] and nums[l] == nums[h]):
                l += 1
                h -= 1

            elif(nums[l] <= nums[mid]):
                if(nums[l] <= target and target < nums[mid]):
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if(target > nums[mid] and nums[h] >= target):
                    l = mid + 1
                else:
                    h = mid - 1

        return False