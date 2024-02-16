class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = [(v, k) for k, v in Counter(arr).items()]
        heapify(heap)
        
        while(k and k >= heap[0][0]):
            k -= heappop(heap)[0]
            
        return len(heap)