class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.getMaxRob(nums[1:]), self.getMaxRob(nums[:-1]))
    
    def getMaxRob(self, nums):
        rob_with, rob_without = 0, 0
        for n in nums:
            newRob = max(rob_with + n, rob_without)
            rob_with = rob_without
            rob_without = newRob

        return rob_without
