class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        es = [(c, e) for e, c in Counter(arr).items()]
        heapify(es)
        
        while(es and es[0][0] <= k):
            c, _ = heappop(es)
            k -= c
        
        return len(es)
        