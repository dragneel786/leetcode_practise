class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        min_sum = max_sum = nums[0]
        tot = curr_min = curr_max = 0
        for num in nums:
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)
            
            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)
            tot += num
        
        return max(max_sum, tot - min_sum) if(min_sum != tot) else max_sum
                
                
        