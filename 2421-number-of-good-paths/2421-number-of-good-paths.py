class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        
        
        def union(x, y):
            px, py = find(x), find(y)
            if(px == py): return
            
            if(vals[px] < vals[py]):
                parent[py] = px
            else:
                parent[px] = py
            
        
        def values_map(size):
            vmap = defaultdict(list)
            for i in range(size):
                vmap[vals[i]].append(i)
                
            return vmap
        
        
        def adj_map(edges):
            tree = defaultdict(list)
            for a, b in edges:
                tree[a].append(b)
                tree[b].append(a)
            return tree
        
        
        def index_and_count():
            for k in sorted(vmap.keys()):
                for v in vmap[k]:
                    for node in tree[v]:
                        if(vals[v] >= vals[node]):
                            union(v, node)
                    
                
                count(vmap[k])
                    
        
        def count(nodes):
            nonlocal ans
            cmap = defaultdict(int)
            for i in nodes:
                cmap[find(i)] += 1
            
            for c in cmap.values():
                ans += (c * (c + 1)) // 2
            
            return ans
        
        n = len(vals)
        ans = 0
        parent = {i:i for i in range(n)}
        vmap = values_map(n)
        tree = adj_map(edges)
        index_and_count()
        return ans
        