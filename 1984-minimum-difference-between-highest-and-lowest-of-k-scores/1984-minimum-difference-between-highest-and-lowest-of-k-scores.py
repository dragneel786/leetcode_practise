class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        min_ans = inf
        for i in range(n - k + 1):
            # print(i)
            min_ans = min(min_ans, nums[k + i - 1] - nums[i])
        
        return min_ans
            