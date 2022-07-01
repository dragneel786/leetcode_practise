class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        costs = 0
        while(len(sticks) > 1):
            st = heappop(sticks) + heappop(sticks)
            costs += st
            heappush(sticks, st)
        return costs
        