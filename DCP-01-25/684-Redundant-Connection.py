class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
                return False
            
            return True

        parent = {i:i for i in range(1, len(edges) + 1)}
        for a, b in edges:
            if union(a, b):
                return [a, b]
        
        return edges[-1]