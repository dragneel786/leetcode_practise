class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        good_idx = n - 1
        for i in range(n - 2, -1, -1):
            if(good_idx <= i + nums[i]):
                good_idx = i
    
        return good_idx == 0
                