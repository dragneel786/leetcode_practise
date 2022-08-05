class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        start = 0
        seen = set()
        chunks = 0
        for i,a in enumerate(arr):
            seen.add(a)
            while(start in seen): start += 1
                
            if(start == i + 1):
                chunks += 1
                
        return chunks
            
            
        