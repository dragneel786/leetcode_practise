class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = ans = streak = 0
        for num in nums:
            if max_val < num:
                max_val = num
                ans = streak = 0
            
            if max_val == num:
                streak += 1
            else:
                streak = 0
            
            ans = max(ans, streak)
        
        return ans