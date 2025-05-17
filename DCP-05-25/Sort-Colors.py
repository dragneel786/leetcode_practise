class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        counts = Counter(nums)
        start = min(counts.keys())
        for i in range(len(nums)):
            nums[i] = start
            counts[start] -= 1
            if counts[start] == 0:
                for i in range(0, 3):
                    if counts[i] == 0:
                        continue
                    start = i
                    break