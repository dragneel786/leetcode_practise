class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        MOD = (10 ** 9) + 7
        ans = 0
        for i, num in enumerate(nums):
            idx = bisect_right(nums, target - num) - 1
            if(idx >= i):
                n = (idx - i)
                ans = (ans + (2 ** n)) % MOD
        
        return ans
        
                
        