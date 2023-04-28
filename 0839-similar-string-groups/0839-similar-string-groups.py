class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def union(x, y):
            parent[x] = y
        
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
            
        def is_similar(w1, w2):
            diff = 0
            for a, b in zip(w1, w2):
                if(a != b):
                    diff += 1
            return diff in [0, 2]
        
        n = len(strs)
        parent = {i:i for i in range(n)}
        for i, a in enumerate(strs):
            for j, b in enumerate(strs):
                if(is_similar(a, b)):
                    pa, pb = find(i), find(j)
                    if(pa != pb):
                        union(pa, pb)
        
        ps = set()
        for i in range(n):
            ps.add(find(i))
        
        return len(ps)
                