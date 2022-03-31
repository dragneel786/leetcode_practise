class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prod = 1
        ans = 0
        j = 0
        for i in range(n):
            prod *= nums[i]
            while(prod >= k and j <= i):
                prod //= nums[j]
                j += 1
            ans += (i - j + 1)
        
        return ans
        
            
            