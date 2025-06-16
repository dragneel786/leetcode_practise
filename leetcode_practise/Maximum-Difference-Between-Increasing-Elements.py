class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        curr_min = nums[0]
        for num in nums[1:]:
            if num > curr_min:
                ans = max(ans, num - curr_min)
            
            else:
                curr_min = min(num, curr_min)
        
        return ans