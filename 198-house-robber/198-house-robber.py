class Solution:
    def rob(self, nums: List[int]) -> int:
        res = nums[0]
        prev = 0
        for i in range(1, len(nums)):
            temp = prev + nums[i]
            if(res < temp):
                prev = res
                res = temp
            else:
                prev = res
        
        return res