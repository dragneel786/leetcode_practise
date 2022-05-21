class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowPrice = 0
        maxProfit = 0
        for i in range(1, n):
            if(prices[lowPrice] > prices[i]):
                lowPrice = i
            maxProfit = max(maxProfit,\
                            prices[i] - prices[lowPrice])
        
        return maxProfit