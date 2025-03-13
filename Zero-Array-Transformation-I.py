class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff_array = [0] * (n + 1)
        for a, b in queries:
            diff_array[a] += 1
            diff_array[b + 1] -= 1

        for i in range(1, n + 1):
            diff_array[i] += diff_array[i - 1]

        for a, b in zip(nums, diff_array):
            if a > b: return False

        return True
