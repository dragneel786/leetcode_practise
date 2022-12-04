class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        def compute(a, b, c, d):
            last = 0
            if(d != 0):
                last = c // d
            return abs(a // b - last)
        
        
        tot = sum(nums)
        prefix = 0
        n = len(nums)
        ans = [inf, -1]
        
        for i, num in enumerate(nums):
            prefix += num
            diff = compute(prefix, i + 1,\
                           tot - prefix, n - i - 1)
            
            if(diff < ans[0]):
                ans = [diff, i]
        
        return ans[1]
                
        