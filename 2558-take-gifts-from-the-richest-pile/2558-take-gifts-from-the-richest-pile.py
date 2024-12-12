class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        heapify(gifts)
        for _ in range(k):
            val = -1 * heappop(gifts)
            heappush(gifts, -floor(val ** 0.5))
        
        return sum([-v for v in gifts])
            
        
        
            
        