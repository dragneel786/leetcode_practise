class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = [0] * 51
        for i in range(len(nums) - k + 1):
            for v in set(nums[i: i + k]):
                counts[v] += 1

        max_val = -1
        for i, c in enumerate(counts):
            if c == 1:
                max_val = i

        return max_val

