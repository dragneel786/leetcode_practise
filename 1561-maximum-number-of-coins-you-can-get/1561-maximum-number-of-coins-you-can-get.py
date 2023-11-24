class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start = 0
        end = len(piles) - 1
        ans = 0
        while(start < end - 1):
            end -= 1
            ans += piles[end]
            end -= 1
            start += 1
    
        return ans