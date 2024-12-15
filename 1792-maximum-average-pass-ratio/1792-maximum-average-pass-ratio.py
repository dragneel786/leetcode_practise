class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def form(a, b):
            return -(((a + 1) / (b + 1)) - (a / b))
        
        heap = [[form(a, b), a, b] for a, b in classes]
        heapify(heap)
        for _ in range(extraStudents):
            _, a, b = heappop(heap)
            a += 1
            b += 1
            heappush(heap, [form(a, b), a, b])
        
        apr = 0
        for _, a, b in heap:
            apr += (a / b)
        
        return apr / len(heap)
    
            
        