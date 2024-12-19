class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        values = arr[:]
        values.sort()
        chunks = idx = 0
        vset = set()
        for i, num in enumerate(arr):
            while(idx < len(arr) and values[idx] in vset):
                idx += 1
            
            chunks += idx == i
            vset.add(num)
        
        return chunks
            
            
            
                
                
        
        
        