class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while(i >= 0):
            j = i + 1
            while(j < n and nums[i] >= nums[j]):
                j += 1

            if(j < n):
                nums[j], nums[i] = nums[i], nums[j]
                break

            nums[i:] = sorted(nums[i:])
            i -= 1

        nums[i + 1:] = sorted(nums[i + 1:])