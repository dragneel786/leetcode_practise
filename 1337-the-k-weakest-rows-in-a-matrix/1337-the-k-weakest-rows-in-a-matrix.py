class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = []
        for row in range(len(mat)):
            idx = bisect.bisect(list(reversed(mat[row])),0)
            counts.append([len(mat[row]) - idx, row])
        
        heapify(counts)
        res = []
        while(k):
            res.append(heappop(counts)[1])
            k -= 1
        return res