class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        i = 0
        while(True):
            while(j < n and nums[j] <= nums[i]):
                j += 1

            if(j >= n):
                break

            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1

        return i + 1