class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        ans = j = 0
        for i, num in enumerate(nums):
            prod *= num
            while(j <= i and prod >= k):
                prod //= nums[j]
                j += 1
            
            ans += (i - j + 1)
        
        return ans