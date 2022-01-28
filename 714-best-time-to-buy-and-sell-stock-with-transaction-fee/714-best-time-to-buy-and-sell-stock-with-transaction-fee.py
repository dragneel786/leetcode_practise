class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bs = -prices[0]
        ss = 0
        for i in range(1, len(prices)):
            temp_bs = max(bs, ss - prices[i])
            temp_ss = max(ss, bs + prices[i] - fee)
            bs = temp_bs
            ss = temp_ss

        return ss