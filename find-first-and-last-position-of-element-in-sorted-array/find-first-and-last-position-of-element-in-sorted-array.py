class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        high = len(nums) - 1
        low = 0
        res = [-1, -1]
        while(low <= high):
            mid = (low + ((high - low)) // 2)
            if(nums[mid] == target):
                res[0] = mid
                high = mid - 1
                print(mid, low, high)

            elif(nums[mid] > target):
                high = mid - 1

            else:
                low = mid + 1

        low, high = 0, len(nums) - 1
        while(low <= high):
            mid = (low + ((high - low)) // 2)
            if(nums[mid] == target):
                res[1] = mid
                low = mid + 1

            elif(nums[mid] > target):
                high = mid - 1

            else:
                low = mid + 1

        return res