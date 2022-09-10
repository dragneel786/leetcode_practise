class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k==0:
            return 0

        if 2*k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        # fill the array
        for i in range(1, n):
            for j in range(k+1):
                # transition equation
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        res = max(dp[n-1][j][0] for j in range(k+1))
        return res
#         def calculate_sell(state, i, remain_tns):
#             val1 = get_me_profit(('B', -1), i + 1, remain_tns - 1)
#             val2 = get_me_profit(state, i + 1, remain_tns)
#             return max(val1 + (prices[i] - state[1]), val2)
        
#         @lru_cache(None)
#         def get_me_profit(state, index, remain_tns):
#             # Base Case.
#             if(not remain_tns or\
#                index >= len(prices)): return 0
            
#             # Recursive function.
#             max_val = 0
#             for i in range(index, len(prices)):
#                 if(state[0] == 'S' and\
#                    state[1] < prices[i]):
#                     max_val = max(max_val, calculate_sell(
#                         state, i, remain_tns))
#                 elif(state[0] == 'B'):
#                     max_val = max(max_val, get_me_profit(
#                         ('S', prices[i]), i + 1, remain_tns))
            
#             return max_val
        
#         return get_me_profit(('B', -1), 0, k)