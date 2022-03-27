class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def getCount(m):
            h = len(m) - 1
            l = 0
            idx = -1
            while(l <= h):
                mid = l + (h - l) // 2
                if(m[mid] == 0):
                    idx = mid
                    h = mid - 1
                elif(m[mid] > 0):
                    l = mid + 1
    
            return idx if(idx != -1) else len(m)
        
        counts = []
        for i in range(len(mat)):
            counts.append([getCount(mat[i]), i])

        res = []
        heapify(counts)
        while(k):
            res.append(heappop(counts)[1])
            k -= 1
        return res
    