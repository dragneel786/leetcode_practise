class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        heap = [(-key, value) for key, value in Counter(nums).items()]
        heapify(heap)
        ans = 0
        while(len(heap) > 1):
            large, count1 = heappop(heap)
            slarge, count2 = heappop(heap)
            ans += count1
            heappush(heap, (slarge, count1 + count2))
        
        return ans