class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cache = defaultdict(lambda:defaultdict(int))
        ans = 0
        
        for i, num in enumerate(nums[1:], 1):
            for j in range(i - 1, -1, -1):
                diff = nums[j] - num
                val = cache[j][diff]
                
                ans += val
                cache[i][diff] += val + 1
        
        return ans
                
        