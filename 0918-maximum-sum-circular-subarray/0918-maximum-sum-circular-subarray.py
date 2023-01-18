class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        right_max = [0] * n
        suffix = right_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix += nums[i]
            right_max[i] = max(suffix, right_max[i + 1])
        
        
        rotate_sum = max_all = curr_max = -1000001
        prefix_sum = 0
        for i, num in enumerate(nums):
            curr_max = max(curr_max + num, num)
            max_all = max(max_all, curr_max)
            
            prefix_sum += num
            if(i + 1 < n):
                rotate_sum = max(rotate_sum,\
                                 prefix_sum + right_max[i + 1])
        
        return max(max_all, rotate_sum)
                
                
                
        