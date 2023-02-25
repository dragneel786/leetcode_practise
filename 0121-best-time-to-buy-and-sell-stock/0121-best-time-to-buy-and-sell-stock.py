class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        bought = inf
        for price in prices:
            if(price < bought):
                bought = price
            max_pro = max(price - bought, max_pro)
        
        return max_pro