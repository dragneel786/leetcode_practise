class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [0] * (m + 1)

        for op in range(m - 1, -1, -1):
            temp = [0] * (m + 1)
            for left in range(op, -1, -1):

                temp[left] = max(
                    multipliers[op] * nums[left] + dp[left + 1],
                    multipliers[op] * nums[n - 1 - (op - left)] + dp[left]
                    )

            dp = temp[:]

        return dp[0]