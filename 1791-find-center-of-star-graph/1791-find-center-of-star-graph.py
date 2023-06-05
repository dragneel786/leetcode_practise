class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        for e in edges[1:]:
            if(a in e):
                return a
            
            if(b in e):
                return b
        
            
            