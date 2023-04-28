class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = py
        
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
            
        def is_similar(w1, w2):
            diff = 0
            for a, b in zip(w1, w2):
                diff += a != b
            return diff in [0, 2]
        
        n = len(strs)
        parent = {i:i for i in range(n)}
        for i, a in enumerate(strs):
            for j, b in enumerate(strs):
                if(is_similar(a, b)):
                    union(i, j)
        
        ps = set()
        for i in range(n):
            ps.add(find(i))
        
        return len(ps)
                