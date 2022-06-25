class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        p, g = [0.0] * n, defaultdict(list)
        for i,e in enumerate(edges):
            a, b = e
            g[a].append((b, i))
            g[b].append((a, i))
        
        p[start] = 1.0
        heap = [(-p[start], start)]
        while(heap):
            prob, v = heappop(heap)
            if(v == end):
                return p[v]
            for ne, i in g[v]:
                if(-prob * succProb[i] > p[ne]):
                    p[ne] = -prob * succProb[i]
                    heappush(heap, (-p[ne], ne))
            
        return 0.0
        