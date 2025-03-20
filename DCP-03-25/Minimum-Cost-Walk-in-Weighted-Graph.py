class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def union(a, b, w):
            pa, wa = find(a)
            pb, wb = find(b)
            # if pa != pb:
            parent[pb] = (pa, wa & wb & w)
            parent[pa] = (pa, wa & wb & w)
        
        def find(a):
            pa, wa = parent[a]
            if a != pa:
                parent[a] = find(pa)

            return parent[a]
        
        parent = {a: (a, 16777215) for a in range(n)}
        for x, y, wg in edges:
            union(x, y, wg)
            # print(x, y, wg, parent)
        
        # print(parent)
        res = []
        for start, end in query:
            ps, ws = find(start)
            pe, we = find(end)
            if ps == pe:
                res.append(ws)
            else:
                res.append(-1)
            
        return res