class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        def make_graph():
            graph = defaultdict(list)
            for [s, e], p in zip(edges, succProb):
                graph[s].append((e, p))
                graph[e].append((s, p))
            return graph
                
        g = make_graph()
        heap = [(1, start)]
        visited = {start:1}
        ans = 0
        while(heap):
            weight, pos = heappop(heap)
            weight = abs(weight)
            if(pos == end):
                return weight
            
            for b, a in g[pos]:
                val = weight * a
                if(visited.get(b, 0) < val):
                    heappush(heap, (-(weight * a), b))
                    visited[b] = val
        
        return ans
            
            
            