class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bs = -prices[0]
        ss = 0
        for i in range(1, len(prices)):
            bs, ss = max(bs, ss - prices[i]), max(ss, bs + prices[i] - fee)
            
        return ss