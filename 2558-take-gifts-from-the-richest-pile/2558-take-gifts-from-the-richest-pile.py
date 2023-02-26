class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        piles = [-g for g in gifts]
        heapify(piles)
        for _ in range(k):
            ele = heappop(piles)
            ele = floor(sqrt(-ele))
            if(ele):
                heappush(piles, -ele)
        
        return -sum(piles)