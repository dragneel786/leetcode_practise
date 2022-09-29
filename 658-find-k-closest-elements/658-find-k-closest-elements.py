class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for a in arr:
            diff = abs(a - x)
            
            if(len(heap) < k or\
               -heap[0][0] > diff):
                
                heappush(heap, (-diff, a))
            
                if(len(heap) > k):
                    heappop(heap)
            
        
        return sorted([b for a, b in heap])