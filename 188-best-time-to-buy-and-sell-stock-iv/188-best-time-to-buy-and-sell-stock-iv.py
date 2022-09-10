class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def calculate_sell(state, index, remain_tns):
            val1 = get_me_profit(('B', -1), index + 1, remain_tns - 1)
            val2 = get_me_profit(state, index + 1, remain_tns)
            return max(val1 + (prices[index] - state[1]), val2)

        def calculate_buy(state, index, remain_tns):
            val1 = get_me_profit(('S', prices[index]), index + 1, remain_tns)
            val2 = get_me_profit(state, index + 1, remain_tns)
            return max(val1, val2)

        def get_me_profit(state, index, remain_tns):
            # Base Case.
            if(not remain_tns or\
                index >= len(prices)): return 0

            # Recursive function.
            key = (state, index, remain_tns)
            if(key in memo):
                return memo[key]
            
            max_val = 0
            if(state[0] == 'S' and state[1] < prices[index]):
                max_val = max(max_val, calculate_sell(
                    state, index, remain_tns))

            elif(state[0] == 'B'):
                max_val = max(max_val, calculate_buy(
                    state, index, remain_tns))

            memo[key] = max_val
            return max_val

        memo = {}
        return get_me_profit(('B', -1), 0, k)