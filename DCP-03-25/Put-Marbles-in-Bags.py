class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        start = 0
        for end in range(len(nums)):
            while(start < end and nums[start] != 0):
                start += 1

            if nums[start] == 0 and nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
        
        return nums

        