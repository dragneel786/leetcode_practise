class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        def construct_graph():
            g = defaultdict(list)
            for w, [a, b] in zip(succProb, edges):
                g[a].append((b, w))
                g[b].append((a, w))
            return g
        
        graph = construct_graph()
        w_visit = [0] * n
        heap = [(-1, start_node)]
        while(heap):
            wei, node = heappop(heap)
            wei = abs(wei)
            if node == end_node:
                return wei
            
            for ne, we in graph[node]:
                if we * wei <= w_visit[ne]:
                    continue
                
                w_visit[ne] = we * wei
                heappush(heap, (-(we * wei), ne))
                
        return 0