class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        ans_set = set([i for i in range(n)])
        for a, b in edges:
            ans_set.discard(b)
        
        return ans_set
            
            
        
        
        