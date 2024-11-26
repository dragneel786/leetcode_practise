class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for a, b in edges:
            in_degree[b] += 1
            
        ans = -1
        counts = 0
        for i, id in enumerate(in_degree):
            if id == 0:
                ans = i
                counts += 1
        
        return ans if counts == 1 else -1
            
        
         