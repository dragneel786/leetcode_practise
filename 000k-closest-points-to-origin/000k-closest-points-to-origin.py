class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        euclid_distance = lambda x, y: (((x - 0) ** 2) +\
                                        ((y - 0) ** 2)) ** 0.5
        
        heap = []
        for x, y in points:
            dis = euclid_distance(x, y)
            if(len(heap) < k or -heap[0][0] > dis):
                heappush(heap, (-dis, [x, y]))
            
            if(len(heap) > k):
                heappop(heap)
        
        return [p for _, p in heap]
            