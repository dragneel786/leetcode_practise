class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(1, n):
            if(nums[j] <= nums[i]):
                continue
                
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1

        return i + 1