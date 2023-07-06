class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = inf
        tot = j = 0
        for i, num in enumerate(nums):
            tot += num
            
            while(tot >= target and j <= i):
                ans = min(abs(i - j + 1), ans)
                tot -= nums[j]
                j += 1
        
        if(tot >= target and j < i):
            ans = min(abs(i - j + 1), ans)
                
        return 0 if(ans == inf) else ans