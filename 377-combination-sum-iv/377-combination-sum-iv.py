class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        nums.sort()
        dp[0] = 1
        for i in range(target + 1):
            for n in nums:
                idx = i - n
                if(idx < 0):
                    break
                dp[i] += dp[idx]

        return dp[target]