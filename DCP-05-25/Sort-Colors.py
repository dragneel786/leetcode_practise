class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        n = len(nums)
        lo = mid = 0
        hi = n - 1
        while(mid <= hi):
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                lo += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1
            
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1

        