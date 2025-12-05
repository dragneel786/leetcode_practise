class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        first = sum(nums)
        ans = second = 0
        for num in nums[:-1]:
            first -= num
            second += num
            if not (abs(first - second) & 1):
                ans += 1
        
        return ans