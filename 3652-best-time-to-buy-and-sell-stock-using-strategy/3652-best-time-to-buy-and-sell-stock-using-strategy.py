class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        prefix = [0] * n
        for i in range(n):
            prefix[i] = prices[i] * strategy[i]
            if i > 0:
                prefix[i] += prefix[i - 1]
        
        tot_k = 0
        half_k = k // 2
        max_val = prefix[-1]
        for i in range(half_k, n):
            tot_k += prices[i]
            if i >= k:
                if i > k:
                    tot_k -= prices[i - half_k]
                max_val = max(max_val, tot_k + prices[-1] - prices[i])
        
        return max_val
        


            
        