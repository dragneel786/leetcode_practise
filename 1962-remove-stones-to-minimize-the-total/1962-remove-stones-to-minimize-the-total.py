class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)
    
        for _ in range(k):
            e = -heappop(heap)
            e = ceil(e / 2)
            heappush(heap, -e)
        
        return -sum(heap)