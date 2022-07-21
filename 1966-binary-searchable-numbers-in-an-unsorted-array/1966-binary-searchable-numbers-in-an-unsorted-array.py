class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        small = [inf] * n
        large = [0] * n
        for i in range(n):
            large[i] = nums[i] if(i == 0) else max(nums[i], large[i - 1])
            small[n - i - 1] = nums[n - i - 1] if(i == 0)\
            else min(nums[n - i - 1], small[n - i])
        
        counts = 0
        for v1, v2 in zip(small, large):
            counts += (v1 == v2)
        return counts