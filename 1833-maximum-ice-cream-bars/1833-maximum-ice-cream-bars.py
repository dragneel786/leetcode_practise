class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        counts = 0
        
        while(costs and costs[0] <= coins):
            coins -= heappop(costs)
            counts += 1
        
        return counts