class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = [-c for c in Counter(arr).values()]
        heapify(heap)
        
        choosed = 0
        remain = len(arr)
        while(heap):
            c = -heappop(heap)
            remain -= c
            choosed += 1
            
            if(remain <= (len(arr) // 2)):
                return choosed
        