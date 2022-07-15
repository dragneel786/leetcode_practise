class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for r in range(min(n, k)):
            heappush(heap, (matrix[r][0], r, 0))
        
        e = -1
        while(k):
            e, r, c = heappop(heap)
            if(c < n - 1):
                heappush(heap, (matrix[r][c + 1], r, c + 1))
            k -= 1
        return e
        
        