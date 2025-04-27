class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        counts = 0
        for i in range(len(nums) - 2):
            counts += (nums[i] + nums[i + 2]) == (nums[i + 1] / 2)
        
        return counts