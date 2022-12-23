class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         def profit(i = 0, buy = True):
#             if(i >= len(prices)):
#                 return 0
            
#             max_profit = 0
#             if(buy):
#                 max_profit = -prices[i] + profit(i + 1, False)
#             else:
#                 max_profit = prices[i] + profit(i + 2, True)
             
#             max_profit = max(max_profit, profit(i + 1, buy))
            
#             return max_profit
        
#         return profit()
    
        n = len(prices)
        dp = [([0] * 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            dp[i][1] = max(dp[i + 1][1],\
                           dp[i + 1][0] - prices[i])
            
            dp[i][0] = max(dp[i + 1][0],\
                           dp[i + 2][1] + prices[i])
        
            
            
        return dp[0][1]
    
        
        
            