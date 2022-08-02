class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return max(a + b for a, b in zip(nums[:n // 2], nums[n//2:][::-1]))