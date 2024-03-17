class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        heap = []
        n = len(arr)
        for a in arr:
            med = arr[(n - 1) // 2]
            heappush(heap, (-abs(a - med), -a))
        
        ans = []
        for _ in range(k):
            ans.append(-heappop(heap)[1])
        
        return ans