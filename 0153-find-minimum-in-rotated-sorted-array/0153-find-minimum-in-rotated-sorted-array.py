class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        start, end = 0, n - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            print(mid)
            if mid == 0:
                if nums[mid] < nums[n - 1]:
                    return nums[mid]
            
            elif mid == n - 1:
                return nums[mid]

            elif nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            
            if nums[mid] > nums[n - 1]:
                start = mid + 1
            else:
                end = mid - 1