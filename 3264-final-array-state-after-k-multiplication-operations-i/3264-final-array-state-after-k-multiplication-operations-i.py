class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(a, i) for i, a in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            val, i = heappop(heap)
            heappush(heap, (val * multiplier, i))
        
        for h, i in heap:
            nums[i] = h
        
        return nums