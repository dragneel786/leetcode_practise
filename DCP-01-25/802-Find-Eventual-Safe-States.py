class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i, a in enumerate(arr):
            for b in arr[i + 1:]:
                heap.append([a / b, a, b])
                
        heap.sort()
        # print(heap)
        return [heap[k - 1][1], heap[k - 1][2]]
    
                
                
        