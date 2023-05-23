class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.size = k
        heapify(self.heap)
        while(len(self.heap) > self.size):
            heappop(self.heap)
        
    def add(self, val: int) -> int:
        if(len(self.heap) < self.size or val > self.heap[0]):
            heappush(self.heap, val)
        
            if(len(self.heap) > self.size):
                heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)