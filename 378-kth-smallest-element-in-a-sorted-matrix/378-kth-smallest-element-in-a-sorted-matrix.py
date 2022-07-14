class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for r in range(n):
            for c in range(n):
                if(not heap or len(heap) < k):
                    heappush(heap, -matrix[r][c])
                elif(-heap[0] > matrix[r][c]):
                    heappop(heap)
                    heappush(heap, -matrix[r][c])
        
        return -heap[0]
        