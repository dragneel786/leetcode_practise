class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp = [[difficulty[i], profit[i]] for i in range(len(profit))]
        dp.sort()
        profits = [x[1] for x in dp]
        curr = 0
        for i in range(len(profits)):
            curr = max(curr, profits[i])
            profits[i] = curr

        res = 0
        for w in worker:
            l, r = 0, len(profit) - 1
            while(l < r):
                mid = (l + r + 1) >> 1
                if(dp[mid][0] <= w):
                    l = mid
                else:
                    r = mid - 1

            res += profits[l] if(dp[l][0] <= w) else 0
        return res
                    
        
        