class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)
        while(len(heap) > 1):
            y, x = -heappop(heap), -heappop(heap)
            heappush(heap, x - y)
        
        return -heap[0]
        