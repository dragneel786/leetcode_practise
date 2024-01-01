class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapify(g)
        heapify(s)
        count = 0
        while(s and g):
            if(s[0] >= g[0]):
                heappop(g)
                count += 1
            
            heappop(s)
        
        return count
        
            
            