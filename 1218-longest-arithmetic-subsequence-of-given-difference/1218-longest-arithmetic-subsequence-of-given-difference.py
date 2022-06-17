class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = defaultdict(lambda:0)
        res = 1
        for i in range(n):
            dp[arr[i]] = dp[arr[i] - difference] + 1
            res = max(dp[arr[i]], res)
        return res