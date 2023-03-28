class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [inf] * (n + 1)
        dp[-2:] = [min(costs), 0]
        for i in range(n - 2, -1, -1):
            for c, d in zip(costs, [0, 6, 29]):
                idx = bisect_right(days, days[i] + d)
                dp[i] = min(dp[idx] + c, dp[i])
        
        # print(dp)
        return dp[0]
        