class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        nums.append(0)
        tot = nums[0]
        max_ans = 0
        for i in range(1, len(nums)):
            if(nums[i] <= nums[i - 1]):
                max_ans = max(tot, max_ans)
                tot = 0
            
            tot += nums[i]
        
        return max_ans