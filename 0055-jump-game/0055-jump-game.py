class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        true_idx = n - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if(i + nums[i] >= true_idx):
                true_idx = i
            
        return true_idx == 0