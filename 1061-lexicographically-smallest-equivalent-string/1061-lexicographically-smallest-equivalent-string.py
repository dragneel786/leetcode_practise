class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def union(x, y):
            parent[y] = x
        
        
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        
        
        def create_map():
            for a, b in zip(s1, s2):
                pa, pb = find(a), find(b)
                if(pa < pb):
                    union(pa, pb)
                else:
                    union(pb, pa)
        
            return parent
    
        parent = {c:c for c in ascii_lowercase}
        create_map()
        return ''.join([find(c) for c in baseStr])
            
        