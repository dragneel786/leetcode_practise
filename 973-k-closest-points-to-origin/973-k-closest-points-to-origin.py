class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        for i in range(n):
            val = ((0 - points[i][0]) ** 2 + (0 - points[i][1]) ** 2) ** 0.5
            points[i] = [val, points[i]]
        
        heapify(points)
        res = []
        
        while(k):
            res.append(heappop(points)[1])
            k -= 1
        
        return res