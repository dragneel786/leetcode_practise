class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while(i > 0):
            j = i
            k = i - 1
            while(j < n and nums[k] >= nums[j]):
                j += 1

            if(j < n):
                nums[j], nums[k] = nums[k], nums[j]
                break

            j = i
            val = nums[i - 1]
            while(j < n and val > nums[j]):
                nums[j - 1] = nums[j]
                j += 1
            nums[j - 1] = val

            i -= 1
        nums[i:] = sorted(nums[i:])