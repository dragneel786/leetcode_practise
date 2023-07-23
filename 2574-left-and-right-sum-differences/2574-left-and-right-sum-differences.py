class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        tot = sum(nums)
        n = len(nums)
        ans = [0 for _ in range(n)]
        ans[0] = tot - nums[0]
        ans[-1] = tot - nums[-1]
        left = 0
        right = ans[0]
        for i in range(1, n - 1):
            left += nums[i - 1]
            right -= nums[i]
            ans[i] = abs(left - right)
        
        return ans