class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        inHand = -prices[0]
        noStock = 0
        for i in range(1, len(prices)):
            tempInHand = max(inHand, noStock - prices[i])
            tempNoStock = max(noStock, sold)
            tempSold = inHand + prices[i]
            inHand = tempInHand
            noStock = tempNoStock
            sold = tempSold

        return max(sold, noStock)
    