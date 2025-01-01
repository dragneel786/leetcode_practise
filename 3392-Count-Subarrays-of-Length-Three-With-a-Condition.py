class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if i >= 2 and (nums[i - 2] + nums[i]) == (nums[i - 1] / 2):
                res += 1
        
        return res
