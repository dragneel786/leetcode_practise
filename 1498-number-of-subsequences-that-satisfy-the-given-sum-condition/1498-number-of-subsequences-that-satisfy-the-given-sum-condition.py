class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        MOD = (10 ** 9) + 7
        ans = 0
        i, j = 0, len(nums) - 1
        while(i <= j):
            if(nums[i] + nums[j] <= target):
                ans += 2 ** (j - i)
                i += 1
            else:
                j -= 1
                
        return ans % MOD
        
                
        