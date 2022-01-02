class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k == 0):
            return 0

        countSubArray = 0
        n = len(nums)
        validProdIdx = 0
        prod = 1
        length = 0
        for i in range(n):
            prod *= nums[i]
            length += 1
            while(validProdIdx <= i and prod >= k):
                prod //= nums[validProdIdx]
                validProdIdx += 1
                length -= 1

            countSubArray += length

        return countSubArray