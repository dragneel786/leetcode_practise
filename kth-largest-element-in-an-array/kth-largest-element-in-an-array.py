class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heap.append(nums[i])
        
        heapify(heap)
        for j in range(k, len(nums)):
            if(heap[0] < nums[j]):
                heappop(heap)
                heappush(heap, nums[j])
        
        return heap[0]
        