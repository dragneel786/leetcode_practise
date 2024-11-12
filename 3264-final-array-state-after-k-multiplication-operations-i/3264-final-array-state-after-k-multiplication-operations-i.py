class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heap.append([num, i])
        
        heapify(heap)
        for _ in range(k):
            val, idx = heappop(heap)
            heappush(heap, [(val * multiplier), idx])
        
        for v, idx in heap:
            nums[idx] = v
        
        return nums
        