class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        heap = []
        
        def push_in_heap(heap, val):
            if(len(heap) < k or heap[0] < val):
                heappush(heap, val)
            
            if(len(heap) > k):
                heappop(heap)
            
        
        for r in range(rows):
            for c in range(cols):
                if(r > 0):
                    matrix[r][c] ^= matrix[r - 1][c]
                
                if(c > 0):
                    matrix[r][c] ^= matrix[r][c - 1]
                
                if(r > 0 and c > 0):
                    matrix[r][c] ^= matrix[r - 1][c - 1]
                
                push_in_heap(heap, matrix[r][c])
        
        return heap[0]
                    
                