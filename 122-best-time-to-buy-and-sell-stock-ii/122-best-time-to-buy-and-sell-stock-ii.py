class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        prices.append(-1)
        total = 0
        for i in range(1, len(prices)):
            if(prices[i - 1] >= prices[i]):
                total += prices[i - 1] - start
                start = prices[i]
            
        return total