class Solution:
    def minOperations(self, nums: List[int]) -> int:
        change = 0
        for idx in range(len(nums) - 2):
            if nums[idx] == 1:
                continue

            for i in range(3):
                nums[idx + i] = 1 - nums[idx + i]
            
            change += 1

        if (0 in nums[-2:]):
            return -1
        return change
    
