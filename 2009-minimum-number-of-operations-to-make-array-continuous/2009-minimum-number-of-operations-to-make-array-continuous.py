class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(set(nums))
        nums.sort()
        ops = j = 0
        for i, num in enumerate(nums):
            while(num > nums[j] + n - 1):
                j += 1
            ops = max(i - j + 1, ops)
        return n - ops
                
        