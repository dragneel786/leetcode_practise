class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        state = [False] * n
        max_v, min_v = -inf, inf
        for i in range(n):
            max_v = max(max_v, nums[i])
            state[i] = max_v == nums[i]
        
        counts = 0
        for i in range(n - 1, -1, -1):
            min_v = min(min_v, nums[i])
            counts += state[i] and min_v == nums[i]
        return counts