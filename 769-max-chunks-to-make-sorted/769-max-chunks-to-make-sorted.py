class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_val = -inf
        chunks = 0
        for i,a in enumerate(arr):
            max_val = max(a, max_val)
            if(max_val == i):
                chunks += 1
        return chunks
            
            
        