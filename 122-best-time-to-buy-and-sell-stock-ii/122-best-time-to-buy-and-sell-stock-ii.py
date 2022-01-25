class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices += [0]
        maxi = prices[0]
        total = 0
        n = len(prices)
        for i in range(1, n):
            if(prices[i - 1] > prices[i]):
                total += (prices[i - 1] - maxi)
                maxi = prices[i]

        return total