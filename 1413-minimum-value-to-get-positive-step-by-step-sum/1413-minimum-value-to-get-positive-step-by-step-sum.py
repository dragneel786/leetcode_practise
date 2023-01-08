class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        val = 0
        ans = 1
        for num in nums:
            val += num
            if(val <= 0):
                ans = max(ans, abs(val) + 1)
        
        return ans