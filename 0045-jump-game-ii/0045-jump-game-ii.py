class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        prev_max = max_reach = jump = 0
        for i in range(n - 1):
            max_reach = max(max_reach, nums[i] + i)
            if(i == prev_max):
                jump += 1
                prev_max = max_reach
        
        return jump
                
                