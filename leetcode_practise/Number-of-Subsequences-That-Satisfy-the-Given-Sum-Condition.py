class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        start, end = 0, len(nums) - 1
        while(start <= end):
            if nums[start] + nums[end] <= target:
                ans = (ans + 2 ** (end - start)) % (10 ** 9 + 7)
                start += 1
            else:
                end -= 1

        return ans
