class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            heap.append((matrix[r][0], r, 0))
        
        heapify(heap)
        prev = 0
        while(k):
            prev, r, c = heappop(heap)
            if(c + 1 < cols):
                heappush(heap, (matrix[r][c + 1], r, c + 1))
            k -= 1
        return prev
        