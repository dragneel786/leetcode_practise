class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = 0
        for c in sorted(costs):
            if(coins < c):
                break
            coins -= c
            counts += 1
        
        return counts