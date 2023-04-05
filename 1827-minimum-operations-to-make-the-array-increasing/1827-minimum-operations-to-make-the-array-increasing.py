class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = prev_val = 0
        for num in nums:
            if(prev_val >= num):
                diff = (prev_val - num + 1)
                prev_val = num + diff
                ans += diff
            else:
                prev_val = num
        
        return ans
                
            