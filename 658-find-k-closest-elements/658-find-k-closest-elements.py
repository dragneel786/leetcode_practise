class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for v in arr:
            heap.append([abs(v - x), v])

        heapify(heap)
        res = []
        while(k):
            res.append(heappop(heap)[1])
            k -= 1

        res.sort()
        return res